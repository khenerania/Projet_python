import stockage
from user import connexion, creer_compte, afficher_historique_utilisateur, sauvegarder_score
from question_qcm import score
from exportation import afficher_menue_exportation
import time
from main_function import (
    afficher_instructions_initiales,
    afficher_page_bienvenue,
    afficher_menu_principal,
    afficher_menu_categories,
    afficher_classement,
    afficher_message_fin,demander_feedback
)
from colorama import init, Fore, Style

# Initialisation de Colorama
init(autoreset=True)

FICHIER_UTILISATEURS = "donne_users.json"

# Charger les utilisateurs existants
users = stockage.charger_donnes_users(FICHIER_UTILISATEURS)

# Afficher la page de bienvenue
afficher_page_bienvenue()

# Afficher le guide initial
afficher_instructions_initiales()

# Vérifiez si l'utilisateur existe
user = None
while not user:
    choix_menu = afficher_menu_principal()
    if choix_menu == '1':
        user = connexion(users)
    elif choix_menu == '2':
        user = creer_compte(users)
        stockage.sauvegarder_donnes_users(users, FICHIER_UTILISATEURS)
    elif choix_menu == '3':
        afficher_classement(users)
    elif choix_menu == '4':
        afficher_message_fin()
        stockage.sauvegarder_donnes_users(users, FICHIER_UTILISATEURS)  # Sauvegarder avant de quitter
        exit()
    else:
        print(Fore.RED + "❌ Choix invalide. Veuillez réessayer." + Style.RESET_ALL)

# Boucle principale de l'application
while True:
    print("\nQue voulez-vous faire?")
    print(Fore.CYAN + "1. Répondre à un QCM" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Voir vos scores précédents" + Style.RESET_ALL)
    print(Fore.CYAN + "3. Classement des scores" + Style.RESET_ALL)
    print(Fore.CYAN + "4. Quitter" + Style.RESET_ALL)
    print(Fore.CYAN + "5. feedback" + Style.RESET_ALL)
    choix_action = input("Votre choix: ")

    if choix_action == '1':
        print(Fore.YELLOW + "🔍 Dans ce QCM, vous devez répondre à des questions de différentes catégories que vous choissisez " + Style.RESET_ALL)
        category, questions = afficher_menu_categories()
        if category and questions:
            print(Fore.GREEN + f"✅ Catégorie choisie: {category}" + Style.RESET_ALL)
            print(Fore.GREEN + f"📋 Nombre de questions à résoudre: {len(questions)}" + Style.RESET_ALL)

            # Début du chronométrage
            start_time = time.time()

            # Calcul du score
            time_limit_per_question = 30
            score_result = score(questions, time_limit_per_question)

            # Fin du chronométrage
            end_time = time.time()

            # Calcul de la durée
            total_time = end_time - start_time
            print(Fore.BLUE + f"\n🕒 Temps total pour compléter le QCM : {total_time:.2f} secondes" + Style.RESET_ALL)

            # Ajouter le score et le temps à l'utilisateur
            sauvegarder_score(user, score_result, category, total_time)  # Passer le temps total
            stockage.sauvegarder_donnes_users(users, FICHIER_UTILISATEURS)

            # Option d'exportation des scores
            afficher_menue_exportation(user)

    elif choix_action == '2':
        print(Fore.YELLOW + "📊 Scores précédents:" + Style.RESET_ALL)
        afficher_historique_utilisateur(user)

    elif choix_action == '3':
        afficher_classement(users)

    elif choix_action == '4':
        afficher_message_fin()
        stockage.sauvegarder_donnes_users(users, FICHIER_UTILISATEURS)
    elif choix_action == '5':
        demander_feedback(user)
        break

    else:
        print(Fore.RED + "❌ Choix invalide, veuillez réessayer." + Style.RESET_ALL)
