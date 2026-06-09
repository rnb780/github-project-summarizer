# Resume Texte

Outil Python simple pour résumer un depot GitHub texte avec une IA via `ollama`.

## Description

Ce projet contient un petit assistant qui lit un fichier `.txt` ou `.json` et envoie le contenu à un modèle IA pour générer un résumé. Le but est d’obtenir un résumé compact, fidèle et adapté aux descriptions de projet technique.

## Structure

- `main.py` : interface en ligne de commande qui liste les fichiers disponibles et demande à l’utilisateur de choisir un fichier à résumer.
- `ouverture_lecteur_fichier.py` : fonction de lecture de fichier avec gestion d’erreur.
- `chatbot_file.py` : construction du prompt système et appel à `ollama.chat` pour générer le résumé.
- `requirements.txt` : dépendance Python nécessaire.

## Installation

1. Assurez-vous d’avoir Python installé (idéalement 3.12+).
2. Installez la dépendance :

```bash
pip install -r requirements.txt
```

3. Configurez l’accès à `ollama` si besoin (authentification / API locale selon votre installation).

## Utilisation

1. Placez votre fichier texte dans le dossier du projet.
2. Lancez le script principal :

```bash
python main.py
```

3. Entrez le nom du fichier lorsque le programme le demande.
4. Le résumé généré s’affichera dans la console.

> Si le fichier n’inclut pas `.txt` ou `.json`, le programme ajoute automatiquement l’extension `.txt`.

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
- Le model `ollama` utilisé pour le test durant le developpement est `llama3`, pour changer de model : `chatbot_file\model=VOTREMODEL`
