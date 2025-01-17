from user import get_history
from question_qcm import score, load_questions
from exportation import export_to_text, display_text_file, display_csv_file, export_to_csv,afficher_menue_exportation
import stockage
import time
from colorama import init, Fore, Style
import json
import os

def afficher_instructions_initiales():
    print('='*90)
    print(Fore.YELLOW + Style.BRIGHT +"                            📝 GUIDE DE L'UTILLISATION  📝")
    print(Fore.RESET + '='*90)
    print("Bienvenue dans l'application de QCM  ! Voici comment utiliser cette application :")
    print("1. Vous pouvez vous connecter ou créer un compte pour accéder aux fonctionnalités.")
    print("2. Une fois connecté, vous pourrez choisir une catégorie de QCM.")
    print("3. Répondez aux questions dans le temps imparti pour chaque question.")
    print("4. Consultez vos scores après chaque session.")
    print("5. Exportez vos scores en fichier texte ou CSV si nécessaire.")
    print("6. Vous pouvez consulter le classement général pour comparer vos résultats avec d'autres.")
    print("Amusez-vous bien et améliorez vos connaissances !")
    input(Fore.CYAN +"\nAppuyez sur Entrée pour continuer vers le menu principal..."+ Style.RESET_ALL)

# Fonction d'affichage de la page de bienvenue
def afficher_page_bienvenue():
    print('='*90)
    print(Fore.GREEN + Style.BRIGHT +"                               🎉 BIENVENUE 🎉                                             ")
    print(Fore.RESET +'='*90)
    print("Bienvenue dans l'application QCM interactive.")
    print("Testez vos connaissances tout en vous amusant !")
    print("Préparez-vous à relever le défi !")
    input(Fore.CYAN +"\nAppuyez sur Entrée pour commencer..."+ Style.RESET_ALL)

# Fonction d'affichage du menu principal
def afficher_menu_principal():
    print('='*90)
    print(Fore.BLUE + Style.BRIGHT +"                                🎓 MENU PRINCIPAL 🎓")
    print(Fore.RESET +'='*90)
    print( "1. Connexion")
    print("2. Créer un compte")
    print("3. Classement des scores")
    print("4. Quitter")
    return input(Fore.CYAN +"Choisissez une option: "+ Style.RESET_ALL)

# Fonction d'affichage du menu de catégorie


def afficher_menu_categories():
    print(Fore.LIGHTBLACK_EX +"\nChoisissez une catégorie de questions:")
    print(Fore.LIGHTBLUE_EX+"1. Complexité")
    print(Fore.LIGHTGREEN_EX+"2. C")
    print(Fore.LIGHTYELLOW_EX+"3. Python")
    category_choice = input(Fore.CYAN +"Votre choix (numéro): "+ Style.RESET_ALL)
    
    if category_choice == '1':
        category = 'Complexité'
        questions = load_questions('question_complexite.json')
    elif category_choice == '2':
        category = 'C'
        questions = load_questions('question_c.json')
    elif category_choice == '3':
        category = 'Python'
        questions = load_questions('question_python.json')
    else:
        print("Choix invalide.")
        return None, None
    
    return category, questions
            

# Fonction pour afficher les instructions
def afficher_instructions():
    print("\n===============================================================================================")
    print("                                  📋 INSTRUCTIONS 📋")
    print("=================================================================================================")
    print("1. Connectez-vous ou créez un compte pour accéder au QCM.")
    print("2. Choisissez une catégorie de questions.")
    print("3. Répondez aux questions dans le délai imparti.")
    print("4. Consultez vos scores et exportez-les si nécessaire.")
    print("5. Améliorez votre score en rejouant les QCM.")
#affichage de classement
def afficher_classement(users):
   
    print('='*90)
    print(Fore.YELLOW + Style.BRIGHT + "                             🏆 CLASSEMENT DES SCORES 🏆")
    print(Fore.RESET+'='*90)
    scores = []
    for user in users:
        for entry in get_history(user):
            scores.append((user['name'], entry['category'], entry['score'], entry.get('time_spent', 'N/A')))
    # Trier par score décroissant (et optionnellement par temps passé croissant en cas d'égalité)
    scores.sort(key=lambda x: (-x[2], x[3] if x[3] != 'N/A' else float('inf')))

    # Afficher les 10 meilleurs
    for i, (name, category, score, time_spent) in enumerate(scores[:10], start=1):
        if time_spent == 'N/A':
            time_display = "Non spécifié"
        else:
            time_display = f"{time_spent} seconde"
        print(Fore.YELLOW + Style.BRIGHT +f"{i}. {name} , categorie {category} : {score} points , ({time_display})")
def afficher_message_fin():
    print(Fore.RED + Style.BRIGHT + "\nMerci d'avoir utilisé l'application QCM !")
    print(Fore.RESET + "Nous espérons que vous avez apprécié votre expérience.")
    print(Fore.GREEN + "À bientôt ! 🎉" + Style.RESET_ALL)
    
def demander_feedback(user):
    """Demande un feedback à l'utilisateur et l'enregistre dans un fichier."""
    print(Fore.YELLOW + "Veuillez donner votre feedback sur l'application (1-5 pour la note, ou un commentaire) : " + Style.RESET_ALL)
    feedback = input("Votre feedback : ")
    print(feedback)

    # Enregistrer le feedback dans un fichier
    with open("feedback.txt", "a") as feedback_file:
        feedback_file.write(f"Feedback de {user['name']} est : {feedback}\n")

    print(Fore.CYAN + "Votre feedback a été enregistré." + Style.RESET_ALL)
