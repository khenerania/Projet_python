import json
import os

FICHIER_UTILISATEURS = "donne_users.json"

# Initialisation du fichier JSON si non existant
def initialiser_fichier_utilisateurs():
    if not os.path.exists(FICHIER_UTILISATEURS):
        with open(FICHIER_UTILISATEURS, 'w') as fichier:
            json.dump({}, fichier)  # Créer un fichier vide avec un dictionnaire


def creer_compte():
    username = input("Entrez un nom d'utilisateur : ").strip()
    password = input("Entrez un mot de passe : ").strip()

    # Charger les données existantes
    with open(FICHIER_UTILISATEURS, 'r+') as fichier:
        utilisateurs = json.load(fichier)
        
        if username in utilisateurs:
            print(" ⚠️ Ce nom d'utilisateur existe déjà. Essayez un autre.")
            return
        
        # Ajouter le nouvel utilisateur
        utilisateurs[username] = {"password": password, "historique": []}
        
        # Sauvegarder les données mises à jour
        fichier.seek(0)
        json.dump(utilisateurs, fichier, indent=4)
        fichier.truncate()
    
    print(" ✅ Compte créé avec succès !")

# pour se connecter
def connexion():
    username = input("Entrez votre nom d'utilisateur : ").strip()
    password = input("Entrez votre mot de passe : ").strip()

    # Charger les données existantes
    with open(FICHIER_UTILISATEURS, 'r') as fichier:
        utilisateurs = json.load(fichier)
        
        if username in utilisateurs and utilisateurs[username]["password"] == password:
            print(f" ✅ Connexion réussie ! Bienvenue, {username}.")
            return username 
        else:
            print(" ⚠️ Nom d'utilisateur ou mot de passe incorrect.")
            return None

# afficher l'historique d'un utilisateur 
def afficher_historique_utilisateur(username):
    with open(FICHIER_UTILISATEURS, 'r') as fichier:
        utilisateurs = json.load(fichier)
        
        if username in utilisateurs:
            print(f"🔍 Historique de {username} :")
            historique = utilisateurs[username]["historique"]
            if not historique:
                print("  Aucun historique disponible.")
            else:
                for session in historique:
                    print(f"  - Date : {session['date']}, Score : {session['score']}")
        else:
            print(" ⚠️ Utilisateur non trouvé.")

