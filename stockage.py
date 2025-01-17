import json
import os
from colorama import init, Fore, Style

# Initialisation de Colorama
init(autoreset=True)

FICHIER_UTILISATEURS = "donne_users.json"

def sauvegarder_donnes_users(users, FICHIER_UTILISATEURS):
    """Sauvegarde les données des utilisateurs dans un fichier JSON."""
    # Vérifie si le fichier existe et charge les utilisateurs existants
    existing_users = []
    if os.path.exists(FICHIER_UTILISATEURS):
        try:
            with open(FICHIER_UTILISATEURS, 'r') as f:
                data = json.load(f)
                existing_users = data.get("users", [])
                
        except json.JSONDecodeError:
            print(Fore.RED + "⚠️ Erreur de décodage JSON : le fichier est peut-être corrompu." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"❌ Une erreur est survenue lors du chargement des données : {e}" + Style.RESET_ALL)

    # Fusionner les nouveaux utilisateurs avec les utilisateurs existants
    for new_user in users:
        for existing_user in existing_users:
            if new_user["name"] == existing_user["name"]:
                existing_user["qcm_history"] = new_user["qcm_history"]
                
                break
        else:
            existing_users.append(new_user)
            

    # Sauvegarder les données mises à jour des utilisateurs dans un fichier JSON
    try:
        with open(FICHIER_UTILISATEURS, 'w') as f:
            json.dump({"users": existing_users}, f, indent=4)
            
    except Exception as e:
        print(Fore.RED + f"❌ Une erreur est survenue lors de la sauvegarde des données : {e}" + Style.RESET_ALL)

def charger_donnes_users(FICHIER_UTILISATEURS):
    """Charge les données des utilisateurs à partir d'un fichier JSON."""
    # Vérifie si le fichier existe
    if os.path.exists(FICHIER_UTILISATEURS):
        # Charge les données des utilisateurs à partir d'un fichier JSON
        try:
            with open(FICHIER_UTILISATEURS, 'r') as f:
                data = json.load(f)
                
                return data.get("users", [])  # Retourne la liste des utilisateurs ou une liste vide
        except json.JSONDecodeError:
            print(Fore.RED + "⚠️ Erreur de décodage JSON : le fichier est peut-être corrompu." + Style.RESET_ALL)
            return []
        except Exception as e:
            print(Fore.RED + f"❌ Une erreur est survenue lors du chargement des données : {e}" + Style.RESET_ALL)
            return []
    else:
        print(Fore.RED + f"❌ Le fichier {FICHIER_UTILISATEURS} n'existe pas." + Style.RESET_ALL)
        return []  # Retourne une liste vide si le fichier n'existe pas

