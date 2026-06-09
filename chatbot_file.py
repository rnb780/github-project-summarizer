"""Outil qui résume un texte avec une IA via Ollama."""

import ollama


def chatbot_fun(text_to_resume):
    # Prompt système pour définir le rôle et le format de sortie de l'IA
    prompt_systeme = [{
        'role': 'system',
        'content': (
            'Tu es une IA spécialisée dans la synthèse des descriptions de projet techniques. Ton unique mission est de produire un résumé fidèle, complet et performant. '
            'Réponds uniquement par un résumé du texte fourni. Ne discute pas, ne poses aucune question et ne fournis aucun commentaire additionnel. '
            'Conserve toutes les informations essentielles : nom du projet, auteur, date, rôle, vision, profil, stack technique, architecture, modules, innovations, gouvernance, sécurité et état du projet. '
            'Utilise un langage clair et précis en français. Préserve les noms techniques, versions, chiffres et termes clés tels qu’ils apparaissent dans le texte. '
            'Regroupe les informations en une réponse structurée et fluide. Tu peux utiliser de courts paragraphes numérotés ou thématiques si cela aide à conserver l’intégralité des points sans perdre en concision. '
            'Ne supprime pas les éléments importants, ne les simplifie pas à l’excès et ne reformule pas de manière à déformer le sens. '
            'Sortie : un seul résumé complet, précis et lisible, qui restitue fidèlement le contenu du texte original.'
        )
    }]

    # Construction du message utilisateur avec le texte à résumer
    demande = prompt_systeme + [{'role':'user','content':f'Fais un résumé de ce texte:\n\n{text_to_resume}'}]

    # Requête vers Ollama
    chatbot = ollama.chat(
        model="llama3",
        messages=demande
    )

    # Affiche le résultat renvoyé par l'IA
    print(chatbot['message']['content'])