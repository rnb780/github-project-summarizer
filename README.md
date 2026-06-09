# Resume Texte

Outil Python simple pour résumer et traduire des dépôts GitHub en français via une IA `ollama`.

## Description

Ce projet contient un assistant intelligent qui lit un fichier `.txt` ou `.json`, peu importe sa langue d'origine, et génère un résumé **fidèle, complet et en français**. Le but est d'obtenir des résumés précis et adaptés aux descriptions de projet technique, en traduisant automatiquement depuis n'importe quelle langue.

## Demonstration CLI

![Project demo avec chinese_test.txt](GIf_demos/Animation_resume.gif)

## Demonstration Web 

![](GIf_demos/Animation_resume_web.gif)

### 🌍 Support Multilingue

L'outil supporte **toutes les langues** : anglais, chinois, allemand, espagnol, et bien d'autres. Que votre fichier soit en anglais, mandarin, ou toute autre langue, il sera résumé et traduit en français avec fidélité.

## Structure

- `main.py` : interface en ligne de commande qui liste les fichiers disponibles et demande à l’utilisateur de choisir un fichier à résumer.
- `ouverture_lecteur_fichier.py` : fonction de lecture de fichier avec gestion d’erreur.
- `chatbot_file.py` : construction du prompt système et appel à `ollama.chat` pour générer le résumé.
- `app.py` : serveur FastAPI qui accepte un upload de fichier et renvoie le résumé de l’IA.
- `interface.py` : interface Streamlit minimale pour afficher un titre et supporter une UI simple.
- `run.py` : script de démarrage tout-en-un qui lance simultanément le backend FastAPI et le frontend Streamlit.
- `requirements.txt` : liste des dépendances Python du projet.

## Architecture

Le projet combine :

- un backend API en `FastAPI` (`app.py`) pour gérer les uploads et les résumés,
- une interface utilisateur légère en `Streamlit` (`interface.py`) pour afficher le résultat.
- un runner tout-en-un (`run.py`) qui démarre à la fois FastAPI et Streamlit.

## Fichiers de Test

Des fichiers de test multilingues sont fournis pour démontrer les capacités de traduction et résumé de l'outil :

- `french_test.txt` : fichier test en français.
- `chinese_test.txt` : fichier test en chinois mandarin.
- `arabic_test.txt` : fichier test en arabe.
- `spanish_test.txt` : fichier test en espagnol.

## Installation

1. Assurez-vous d’avoir Python installé (idéalement 3.12+).
2. Installez les dépendances du projet :

```bash
pip install -r requirements.txt
```

3. Configurez l’accès à `ollama` si besoin (authentification / API locale selon votre installation).

4. Vérifiez que `uvicorn` et `streamlit` sont installés :

```bash
uvicorn --version
streamlit --version
```

## Utilisation

### Mode ligne de commande

1. Placez votre fichier texte dans le dossier du projet.
2. Lancez le script principal :

```bash
python main.py
```

3. Entrez le nom du fichier lorsque le programme le demande.
4. Le résumé généré **en français** s'affichera dans la console.

> Si le fichier n'inclut pas `.txt` ou `.json`, le programme ajoute automatiquement l'extension `.txt`.

### Mode tout-en-un avec `run.py`

1. Lancez le script de démarrage tout-en-un :

```bash
python run.py
```

2. Ce script démarre en parallèle :
   - le backend FastAPI (`app.Py`) via `uvicorn`
   - le frontend Streamlit (`interface.py`)

3. Ouvrez l’URL affichée par Streamlit dans votre navigateur pour accéder à l’interface.

### Exemple avec Traduction

Vous pouvez tester avec les fichiers multilingues fournis :

```bash
python main.py
# Entrez : chinese_test (résumé en français depuis le chinois)
# Ou : arabic_test (résumé en français depuis l'arabe) etc...
# Le résumé s'affichera automatiquement en français
```

## Cas d'Usage Principaux

- **Résumer des dépôts GitHub** : Clonez un dépôt, récupérez son README ou sa documentation, et obtenez un résumé fidèle en français.
- **Traduire et résumer** : Convertissez et résumez des documents en anglais, mandarin, allemand, etc. vers le français en une seule opération.
- **Traiter des documents multilingues** : L'outil maintient l'intégrité du contenu tout en forçant la sortie en français.

## Désinstallation

Pour supprimer l’outil localement, supprimez simplement le dossier du projet ou les fichiers suivants :

- `main.py`
- `chatbot_file.py`
- `ouverture_lecteur_fichier.py`
- `requirements.txt`
- `README.md`
- tout fichier `.txt` ou `.json` que vous avez ajouté pour test

Pour désinstaller la dépendance Python :

```bash
pip uninstall ollama
```

## Notes

- Le projet suppose que `ollama` est correctement configuré sur votre machine.
- Si vous utilisez une autre version de Python, adaptez la commande `python` en conséquence (`python3`, `py`, etc.).
- Le modèle `ollama` utilisé pour le test durant le développement est `llama3`. Pour changer de modèle : `chatbot_file.py` → `model="VOTREMODEL"`
- **L'outil FORCE la sortie en français** : Peu importe la langue du fichier source, la réponse sera toujours en français.
- Les fichiers de test `french_test.txt`, `chinese_test.txt` et `arabic_test.txt` sont fournis pour valider la traduction multilingue.
- --- Outil en phase de **développement** ---
