from user import creer_compte, connexion, initialiser_fichier_utilisateurs, afficher_historique_utilisateur
from qcm_game import jouer_qcm
from question_qcm import load_questions

# Initialiser le fichier JSON des utilisateurs
initialiser_fichier_utilisateurs()

# Fonction d'affichage de la page de bienvenue
def afficher_page_bienvenue():
    print("\n====================================")
    print("          🎉 BIENVENUE 🎉           ")
    print("====================================")
    print("Testez vos connaissances avec ce QCM interactif !")
    input("\nAppuyez sur Entrée pour continuer...")

# Fonction d'affichage du guide d'utilisation
def afficher_guide_utilisation():
    print("\n====================================")
    print("        📘 GUIDE D'UTILISATION 📘    ")
    print("====================================")
    print("Bienvenue dans l'application de QCM. Voici comment l'utiliser :")
    print("1. **Connexion** : Connectez-vous en saisissant votre nom d'utilisateur et mot de passe.")
    print("2. **Créer un compte** : Si vous n'avez pas de compte, créez-en un pour commencer.")
    print("3. **Jouer au QCM** : Choisissez une catégorie et répondez aux questions proposées.")
    print("4. **Afficher l'historique** : Consultez vos performances précédentes après connexion.")
    print("5. **Quitter** : Fermez l'application.")
    print("\n**Conseils :**")
    print("- Vos scores sont automatiquement enregistrés après chaque session.")
    print("- Assurez-vous que tous les fichiers nécessaires (.json) sont présents.")
    print("- Consultez régulièrement vos performances pour vous améliorer !")
    input("\nAppuyez sur Entrée pour retourner au menu principal...")

# Fonction d'affichage du menu principal
def afficher_menu_principal():
    print("\n====================================")
    print("         🎓 MENU PRINCIPAL 🎓       ")
    print("====================================")
    print("1. Connexion")
    print("2. Créer un compte")
    print("3. Jouer au QCM")
    print("4. Afficher l'historique")
    print("5. Quitter")
    print("6. Guide d'utilisation")  
    return input("Choisissez une option : ")

def main():
    afficher_page_bienvenue()
    utilisateur_connecte = None

    while True:
        choix = afficher_menu_principal()

        if choix == "1": 
            utilisateur_connecte = connexion()
        elif choix == "2":  
            creer_compte()
        elif choix == "3":  
            if utilisateur_connecte:
                jouer_qcm(utilisateur_connecte)
            else:
                print("⚠️ Veuillez vous connecter d'abord.")
        elif choix == "4": 
            if utilisateur_connecte:
                afficher_historique_utilisateur(utilisateur_connecte)
            else:
                print("⚠️ Veuillez vous connecter d'abord.")
        elif choix == "5":  
            print("👋 Merci d'avoir utilisé l'application. Au revoir !")
            break
        elif choix == "6":  
            afficher_guide_utilisation()
        else:
            print("⚠️ Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
