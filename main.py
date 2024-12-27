# Fonction d'affichage des instructions initiales
def afficher_instructions_initiales():
    print("\n=========================================================================================")
    print("                            📝 GUIDE DE L'UTILISATEUR 📝")
    print("============================================================================================")
    print("Bienvenue dans l'application de QCM ! Voici comment utiliser cette application :")
    print("1. Vous pouvez vous connecter ou créer un compte pour accéder aux fonctionnalités.")
    print("2. Une fois connecté, vous pourrez choisir une catégorie de QCM.")
    print("3. Répondez aux questions dans le temps imparti pour chaque question.")
    print("4. Consultez vos scores après chaque session.")
    print("5. Exportez vos scores en fichier texte ou CSV si nécessaire.")
    print("6. Vous pouvez consulter le classement général pour comparer vos résultats avec d'autres.")
    print("Amusez-vous bien et améliorez vos connaissances !")
    input("\nAppuyez sur Entrée pour continuer vers le menu principal...")

# Fonction d'affichage de la page de bienvenue
def afficher_page_bienvenue():
    print("\n==========================================================================================")
    print("                               🎉 BIENVENUE 🎉                                             ")
    print("============================================================================================")
    print("Bienvenue dans l'application QCM interactive.")
    print("Testez vos connaissances tout en vous amusant !")
    print("Préparez-vous à relever le défi !")
    input("\nAppuyez sur Entrée pour commencer...")

# Fonction d'affichage du menu principal
def afficher_menu_principal():
    print("\n===========================================================================================")
    print("                                🎓 MENU PRINCIPAL 🎓")
    print("=============================================================================================")
    print("1. Connexion")
    print("2. Créer un compte")
    print("3. Instructions")
    print("4. Classement des scores")
    print("5. Quitter")
    return input("Choisissez une option: ")

# Fonction d'affichage du menu de catégorie
def afficher_menu_categories():
    print("\nChoisissez une catégorie de questions:")
    print("1. Complexité")
    print("2. C")
    print("3. Python")
    return input("Votre choix (numéro): ")

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
