import pickle
import datetime
from collections import defaultdict, Counter
from nltk.tokenize import word_tokenize

class MarkovLanguageModel:
    def __init__(self, order=2):
        self.order = order  # 2 = trigramme (dépend des 2 mots précédents)
        self.ngram_counts = defaultdict(Counter)
        self.context_counts = Counter()
    
    def train(self, sentences):
        for sent in sentences:
            tokens = word_tokenize(sent.lower())
            # Ajout de marqueurs de début/fin
            tokens = ["<s>"] * (self.order - 1) + tokens + ["</s>"]
            # Générer tous les n-grammes
            for i in range(self.order - 1, len(tokens)):
                context = tuple(tokens[i - self.order + 1:i])  # ex. (w_{i-2}, w_{i-1})
                word = tokens[i]
                self.ngram_counts[context][word] += 1
                self.context_counts[context] += 1

    def probability(self, word, context):
        """Retourne P(word | context)"""
        context = tuple(context)
        if self.context_counts[context] == 0:
            return 0.0
        # Lissage de Laplace (ajout de 1 pour éviter zéro)
        vocab_size = len(self.context_counts)  # approximation simplifiée
        return (self.ngram_counts[context][word] + 1) / (
            self.context_counts[context] + vocab_size
        )

    def predict_next(self, context, top_k=3):
        """Prédire les k mots les plus probables après `context`"""
        context = tuple(context[-(self.order - 1):])  # garder seulement l'historique nécessaire
        if context not in self.ngram_counts:
            return []  # ou retourner des mots par défaut selon la structure VOS
        candidates = self.ngram_counts[context].most_common(top_k)
        return [word for word, _ in candidates]


# Exemple de corpus malgache (VOS)

corpus = []

output_file = "data/bible_malgache_phrases.txt"
with open(output_file, "r", encoding="utf-8") as f:
    for line in f:
        phrase = line.strip()  # Supprime les sauts de ligne et espaces inutiles
        if phrase:  # Ignore les lignes vides
            corpus.append(phrase)


# ------------------
# Entraînement
# ------------------
model = MarkovLanguageModel(order=3)  # trigramme = ordre 3 → dépend des 2 mots précédents
model.train(corpus)

model2 = MarkovLanguageModel(order=2)
model2.train(corpus)

# ------------------
# Prédiction
# ------------------
print("Après 'tonga' →", model2.predict_next(["tonga"]))

# Supposons que 'model' est votre instance entraînée
now = datetime.datetime.now().strftime("%Y%m%d")
filename = f"models/malagasy_markov_model_2_v1_{now}.pkl"
filename2 = f"models/malagasy_markov_model_3_v1_{now}.pkl"

with open(filename, "wb") as f:
    pickle.dump(model, f)

with open(filename2, "wb") as f:
    pickle.dump(model2, f)

print("✅ Modèle sauvegardé dans 'malagasy_markov_model.pkl'")
