"""Lecteur de fichier simple pour retourner le contenu texte d'un fichier."""
import os


def lecture(fichier):
    # Ouvre le fichier en mode lecture UTF-8
    try:
        with open(fichier, 'r', encoding='UTF8') as f:
            entier = f.read()
            if entier.strip():
                return entier
            else:
                # Fichier vide : on renvoie None pour indiquer un échec
                print(f"Erreur : le fichier '{fichier}' est vide")
                return None
    except FileNotFoundError:
        # Fichier non trouvé
        print(f"Erreur : le fichier '{fichier}' n'existe pas")
        return None
    except Exception as e:
        # Autres erreurs lors de la lecture du fichier
        print(f"Erreur : {e}")
        return None

