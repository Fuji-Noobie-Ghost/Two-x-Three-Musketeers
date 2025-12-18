# **IAMA_Project**

## **Examen Clinique TP Intelligence Artificielle**

Réalisé au sein de ISPM - Madagascar (www.ispm-edu.com)

## Éditeur de Texte Augmenté par l'IA pour le Malagasy
Un éditeur intelligent conçu spécifiquement pour la langue malgache, combinant des approches hybrides pour pallier le manque de données.


## **Nom du projet : IAMA**

### **1\. Informations sur le Groupe**

#### Membre 1 : 
* nom : ANDRIAMANALINA 
* prénom(s) : Rita Harenah
* classe : ESIIA 5
* numéro : 05
* rôle : *Ontology Engineer*

#### Membre 2 : 
* nom : RAKOTONOELINA 
* prénom(s) : Lala Minoniaina Joannah
* classe : ESIIA 5
* numéro : 09
* rôle : *Frontend (UX/UI)*

#### Membre 3 : 
* nom : RAKOTONJANAHARY
* prénom(s) : Miora Irinah
* classe : ESIIA 5
* numéro : 10
* rôle : *Frontend (UX/UI)*

#### Membre 4 : 
* nom : RATOVONARIVO
* prénom(s) : Zo Michaël 
* classe : ESIIA 5
* numéro : 15
* rôle : *Ontology Engineer, Data Engineer, Algo*

#### Membre 5 : 
* nom : ANDRIAMIHAJA
* prénom(s) : Alan Steven
* classe : ESIIA 5
* numéro : 16
* rôle : *Data Engineer, DevOps*

#### Membre 6 : 
* nom : RATIA ANDRIAFITAHIANA
* prénom(s) : Joseph Tellia
* classe : ESIIA 5
* numéro : 19
* rôle : *Lead Backend, DevOps*

### **2\. Documentation Technique**
> #### 2.1 *Résumé des Algorithmes clés*
| Algorithme               | Type                       | Complexité      | Optimisations                     |
|--------------------------|----------------------------|----------------|----------------------------------|
| Correcteur Hybride       | Mixte (Symbolique + Statistique) | O(n*m)         | Cache, seuils, indexation        |
| Lemmatiseur              | Symbolique (Règles)       | O(n*k)         | Arbres de préfixes, exceptions   |
| Autocomplétion N-Gram    | Statistique               | O(1) prédiction | Pré-calcul, compression           |
| Analyse Sentiment        | Basé règles               | O(n)           | Listes de mots-clés, intensificateurs |
| Fusion Résultats         | Méta-algorithme           | O(s)           | Pondération, résolution conflits |

Ces algorithmes sont conçus spécifiquement pour les langues à faibles ressources comme le malagasy, avec un accent sur la robustesse, l'efficacité et la capacité à fonctionner avec peu de données.

> #### 2.2 *Architecture Globale*
> - Vue d'Ensemble
> - Flux de Données

> #### 2.3 *Technologie*
> - Backend (FastAPI)
> - Frontend (React)

### **3\. Fonctionnalité IA Implémentées**

> #### 3.1 *Correcteur Orthographique Hybride*
   > - Distance de Levenshtein optimisée avec RapidFuzz
   > - Règles phonotactiques malgaches (nb, mk, nk interdits)
   > - Dictionnaire de 10,000+ mots scrapés de Wikipedia MG

> #### 3.2 *Lemmatiseur Basé Règles*
   > - Détection des préfixes (mi-, ma-, man-, etc.)
   > - Détection des suffixes (-ana, -ina, -na)
   > - Extraction de racines avec validation

> #### 3.3 *Autocomplétion Intelligente*
   > - Modèle trigramme entraîné sur spacy
   > - Suggestions contextuelles
   > - Prédiction de mots suivants

> #### 3.4 *Traduction Mot-à-Mot*
   > - Dictionnaire malgache-français local
   > - Popup au clic droit
   > - Pas de dépendance API externe








**🔗 Liens Utiles :**


