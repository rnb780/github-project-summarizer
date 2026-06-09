from ouverture_lecteur_fichier import lecture
from chatbot_file import chatbot_fun
import os

# Liste des fichiers disponibles dans le dossier courant
# Seules les extensions .txt et .json sont prises en compte
tout_element = os.listdir(".")
fichiers_txt = [f for f in tout_element if f.endswith(".txt") or f.endswith(".json")]


def main():
    # Boucle principale du programme
    while True :
        print(f"\nfichiers disponibles : {fichiers_txt}")
        print("Tapez '0' pour quitter")
        question = input("Nom du fichier : ").strip()

        if question == '0':
            break

        if not question.endswith('.txt') and not question.endswith('.json'):
            question += '.txt'

        # Lecture du contenu du fichier choisi si present dans le dossier
        if question in fichiers_txt :
            lecture_fichier = lecture(question)
        else : 
            print("Veuillez placer le texte dans le dossier.")
            continue
        if lecture_fichier :
            # Appel au module de resume IA
            chatbot_fun(lecture_fichier)
        else : 
            print(f"fichier {question} indisponible, veuillez verifier")
        

if __name__ == "__main__":
    # Point d'entree du script
    main()