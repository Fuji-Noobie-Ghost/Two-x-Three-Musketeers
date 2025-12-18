import re
import nltk
import glob

# Donnees venant de https://nybaiboly.net

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def clean_malgache_bible(text):
    lines = text.splitlines()
    clean_lines = []
    in_header = True  # on ignore tout jusqu'à "Chapitre 1"

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Démarrer à partir de "Chapitre 1"
        if "Chapitre 1" in line:
            in_header = False
            continue

        if in_header:
            continue

        if line == "*":
            continue

        # Ignorer les "Chapitre X"
        if re.match(r'^Chapitre\s+\d+', line):
            continue

        # Supprimer les numéros de verset en début de ligne (ex: "1 ", "23 ")
        line = re.sub(r'^\d+\s*', '', line)

        # Supprimer les crochets [annotation]
        line = re.sub(r'\[.*?\]', '', line).strip()

        if line:
            clean_lines.append(line)

    return "\n".join(clean_lines)

def split_into_sentences(text):
    """Découpe un texte en phrases (avec nltk)"""
    # NLTK ne connaît pas le malgache → on utilise la ponctuation standard
    sentences = nltk.sent_tokenize(text, language='french')  # meilleure approximation
    # Nettoyer les espaces et sauts de ligne
    sentences = [re.sub(r'\s+', ' ', sent).strip() for sent in sentences]
    # Filtrer les phrases trop courtes ou non alphabétiques
    sentences = [s for s in sentences if len(s) >= 10 and re.search(r'[a-zA-Z]', s)]
    return sentences


files = [
    "deuteronome_malgache_propre.txt",
    "exode_malgache_propre.txt",
    "genese_malgache_propre.txt",
    "josue_malgache_propre.txt",
    "juges_malgache_propre.txt",
    "levitique_malgache_propre.txt",
    "nombres_malgache_propre.txt",
    "ruth_malgache_propre.txt"
]

# Sauvegarder les phrases (une par ligne)
output_file = "data/bible_malgache_phrases.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for file in glob.glob('data/bible_cleaned/*.txt'):
        with open(file, "r", encoding="utf-8", errors="ignore") as f2:
            raw_text = f2.read()

        cleaned = clean_malgache_bible(raw_text)

        print("✂️  Découpage en phrases...")
        sentences = split_into_sentences(cleaned)

        for sent in sentences:
            f.write(sent + "\n")

print("✅ Dataset nettoyé et prêt à l’usage !")
