# Projet AI RAG

**Langage utilisé** : Python

**RAG (Retriever-Augmented Generation)** est une méthode qui permet d'améliorer les capacités des modèles de langage (LLM) en combinant leur compréhension du langage avec une récupération ciblée d'informations pertinentes provenant de sources externes, souvent en utilisant des embeddings dans des bases de données vectorielles. Cela conduit à des applications alimentées par l'IA plus précises, fiables et polyvalentes.

## Comment exécuter le projet :

### **Lancer le projet avec RAG :**

**Installer les dépendances du projet :**

```bash
make install
```

Cette commande crée un environnement virtuel, installe toutes les dépendances Python nécessaires et télécharge les embeddings du modèle. Elle télécharge également un fichier PDF depuis Dropbox et en extrait le contenu dans `petitprince.txt`.

> _Optionnel :_ Vous pouvez consulter le contenu de `petitprince.txt` en utilisant la commande suivante :

```bash
cat petitprince.txt
```



**Exécuter le projet :**

```bash
make start
```

Cette commande lance le chatbot où vous pouvez poser des questions sur le fichier téléchargé (dans ce cas, le contenu extrait du PDF "Le Petit Prince"). Le chatbot utilise la technique RAG pour extraire le contexte pertinent du document et générer des réponses plus précises.

> **IMPORTANT**  
> Les requêtes sur des sujets non liés au contenu du PDF peuvent entraîner des réponses inexactes, car le modèle se concentre sur les informations du document.

**Nettoyer les fichiers temporaires :**

```bash
make clean
```

Cette commande supprime le fichier `petitprince.txt` et nettoie l'environnement virtuel.

---

## Structure du projet

```
.
├── .venv/                     # Environnement virtuel
├── Makefile                   # Makefile pour automatiser l'installation, l'exécution et le nettoyage
├── localrag.py                # Script principal pour traiter les requêtes avec Ollama et RAG
├── upload.py                  # Script pour télécharger et traiter le PDF depuis Dropbox
├── petitprince.txt            # Contenu extrait du PDF
├── requirements.txt           # Liste des dépendances
├── README.md                  # Ce fichier
└── vault_embeddings.pth       # Embeddings pour le contenu du document
```

---

## Notes :

1. **RAG avec Ollama** : Ce projet utilise **Ollama** pour générer des réponses en fonction du contexte du document. Les embeddings sont calculés à partir du document et utilisés pour trouver les informations pertinentes pour générer des réponses plus précises.
2. **Personnalisation** : Vous pouvez modifier le service cloud ou la source du PDF (dans `upload.py`) si vous préférez utiliser un autre service de stockage que Dropbox.

3. **Réglage de la température** : Vous pouvez ajuster le paramètre `temperature` dans la configuration du modèle pour contrôler la créativité des réponses. Des valeurs faibles (par exemple, 0.1) rendent les réponses plus déterministes, tandis que des valeurs plus élevées (par exemple, 0.7) donnent des réponses plus créatives.

---

## La question poser a ete

Comment le petit prince en vient-il à comprendre que sa rose est unique ?
