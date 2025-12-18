import json
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import List, Dict, Any
import json
import utils
from rapidfuzz import process, fuzz

app = FastAPI(
    title="Éditeur Malagasy - API IA",
    description="API pour correcteur orthographique et suggestions en malgache",
    version="1.0.0"
)

# Chargement du lexique au démarrage
try:
    with open("data/malagasy_lexicon.json", "r", encoding="utf-8") as f:
        malagasy_data: List[Dict[str, Any]] = json.load(f)
        MALAGASY_WORDS = [entry["malagasy"] for entry in malagasy_data]
        WORD_TO_ENTRY = {entry["malagasy"]: entry for entry in malagasy_data}
except FileNotFoundError:
    print("❌ Fichier non trouvé. Lancez d'abord le scraper.")
    malagasy_data = []
    MALAGASY_WORDS = []
    WORD_TO_ENTRY = {}
except json.JSONDecodeError:
    print("❌ Fichier JSON corrompu.")
    malagasy_data = []
    MALAGASY_WORDS = []
    WORD_TO_ENTRY = {}

class BusinessLogicException(Exception):
    def __init__(self, message: str = "", data = [], status_code: int = 500):
        self.status_code = status_code
        self.message = message
        self.data = data

@app.exception_handler(BusinessLogicException)
async def business_logic_exception_handler(request: Request, exc: BusinessLogicException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.message, "data": exc.data},
    )

class BusinessLogicResponse():
    def __init__(self, status_code: int = 200, message: str = "", data = []):
        self.message = message
        self.status_code = status_code
        self.data = data

    def send(self):
        return JSONResponse(
            status_code = self.status_code,
            content={"success": True, "message": self.message, "data": self.data},
        )

# --- Endpoints ---

@app.get("/dico", response_model=List[Dict[str, Any]])
def get_dictionaries():
    """Renvoie tout le dictionnaire malagasy."""
    if not malagasy_data:
        raise HTTPException(status_code=500, detail="Lexique non chargé")
    return malagasy_data 


@app.get("/check")
def check_word(w: str = Query(..., description="Mot à valider")):
    """Valide un mot malagasy selon des règles linguistiques."""
    is_success = utils.mot_valide(w)
    return {"success": is_success}


@app.get("/autocomplete")
def get_autocompletions(
    word: str = Query(..., description="Mot avec ou sans faute"),
    limit: int = Query(5, ge=1, le=10, description="Nombre max de suggestions")
):
    """Renvoie des suggestions de mots malagasy proches (fuzzy matching)."""
    if not utils.mot_valide(word):
        raise BusinessLogicException(status_code=422, message="Ce n'est pas un mot Malagasy valide")
    if not MALAGASY_WORDS:
        raise BusinessLogicException(status_code=500, message="Lexique non chargé")

    results = process.extract(
        word,
        MALAGASY_WORDS,
        scorer=fuzz.WRatio,
        limit=limit
    )

    suggestions = []
    for match, score, _ in results:
        if score >= 60:
            entry = WORD_TO_ENTRY.get(match)
            if entry:
                suggestions.append({
                    "malagasy": match,
                    "francais": entry["francais"],
                    "anglais": entry["anglais"],
                    "score": round(score, 2)
                })

    return BusinessLogicResponse(data=suggestions).send()


# Lancement (optionnel – généralement géré par `uvicorn`)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
