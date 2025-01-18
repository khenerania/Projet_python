from datetime import datetime
import time
from colorama import init, Fore, Style

# Initialisation de Colorama
init(autoreset=True)

def sauvegarder_score(user, score, category, time_spent):
    if 'qcm_history' not in user:
        user['qcm_history'] = []
    user['qcm_history'].append({
        'category': category,
        'score': score,
        'date': time.strftime("%Y-%m-%d %H:%M:%S"),
        'time_spent': time_spent  # Ajouter le temps passé
    })
    print(Fore.GREEN + f"✅ Score de {score} points sauvegardé pour la catégorie '{category}'." + Style.RESET_ALL)

def get_history(user):
    # Retourne l'historique des QCM de l'utilisateur
    return user["qcm_history"]

def connexion(utilisateurs):
    """Gère la connexion."""
    username = input(Fore.CYAN + "Entrez votre nom d'utilisateur : " + Style.RESET_ALL).strip()
    
    # Vérifie si l'utilisateur existe
    for user in utilisateurs:
        if user["name"] == username:
            for tentative in range(3):  # Boucle pour les 3 tentatives
                password = input(Fore.CYAN + "Entrez votre mot de passe : " + Style.RESET_ALL).strip()
                if password == user["password"]:
                    print(Fore.GREEN + f"🎉 Bienvenue une autre fois, {username} !" + Style.RESET_ALL)
                    if 'qcm_history' in user:
                        print("📜 Historique des QCM:")
                        afficher_historique_utilisateur(user)
                    else:
                        print("❌ Aucun historique pour le moment.")
                    return user  # Connexion réussie
                else:
                    print(Fore.RED + f"❌ Mot de passe incorrect. Tentative {tentative + 1}/3." + Style.RESET_ALL)
            print(Fore.RED + f"🚫 Nombre maximum de tentatives atteint pour {username}. Accès refusé." + Style.RESET_ALL)
            return None  # Nombre maximum de tentatives atteint
    print(Fore.RED + "❌ Utilisateur non trouvé ! Vous devez créer un compte." + Style.RESET_ALL)
    return None

def creer_compte(utilisateurs):
    name = input(Fore.CYAN + "Entrez votre nom pour créer un compte: " + Style.RESET_ALL)
    
    while True:
        password = input(Fore.CYAN + "Entrez un mot de passe (au moins 4 caractères) : " + Style.RESET_ALL).strip()
        if len(password) < 4:
            print(Fore.RED + "⚠️ Le mot de passe doit contenir au moins 4 caractères." + Style.RESET_ALL)
        else:
            break
    user_names = [u["name"] for u in utilisateurs]
    if name in user_names:
        print(Fore.RED + "⚠️ Ce nom est déjà utilisé. Veuillez vous connecter ou changer de nom d'utilisateur." + Style.RESET_ALL)
        return None
    else:
        user = {
            "name": name,
            "password": password,
            "qcm_history": []
        }
        utilisateurs.append(user)
        print(Fore.GREEN + f"✅ Compte créé avec succès pour {user['name']}!" + Style.RESET_ALL)
        return user

def afficher_historique_utilisateur(user):
    if not user['qcm_history']:
        print(Fore.YELLOW + "📜 Aucun historique disponible." + Style.RESET_ALL)
        return
    for entry in get_history(user):
        print(Fore.LIGHTGREEN_EX + f"Catégorie: {entry['category']}, Score: {entry['score']}, Temps passé: {entry.get('time_spent', 'N/A')}s, Date: {entry['date']}" + Style.RESET_ALL)
