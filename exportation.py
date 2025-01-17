import csv
import stockage
from user import get_history
from colorama import init, Fore, Style

# Initialisation de Colorama
init(autoreset=True)

def export_to_text(user):
    """Exporte les scores de l'utilisateur dans un fichier texte."""
    if not user:
        print(Fore.RED + "❌ Utilisateur non spécifié pour l'exportation." + Style.RESET_ALL)
        return

    with open("scores.txt", "w") as file:
        file.write(f"Scores pour {user['name']} :\n")
        file.write('='*20)
        for entry in user.get("qcm_history", []):
            time_spent = entry.get("time_spent", "Non spécifié")
            file.write(f"Date: {entry['date']}, Catégorie: {entry['category']}, Score: {entry['score']}, Temps passé: {time_spent} sec\n")

    print(Fore.GREEN + "✅ Scores exportés dans 'scores.txt'." + Style.RESET_ALL)

def export_to_csv(user):
    """Exporte les scores de l'utilisateur dans un fichier CSV."""
    if not user:
        print(Fore.RED + "❌ Utilisateur non spécifié pour l'exportation." + Style.RESET_ALL)
        return

    with open("scores.csv", "w", newline='') as csvfile:
        fieldnames = ["Date", "Catégorie", "Score", "Temps passé (sec)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in user.get("qcm_history", []):
            writer.writerow({
                "Date": entry['date'],
                "Catégorie": entry['category'],
                "Score": entry['score'],
                "Temps passé (sec)": entry.get("time_spent", "Non spécifié")
            })
    print(Fore.GREEN + "✅ Scores exportés dans 'scores.csv'." + Style.RESET_ALL)

def display_text_file(file_path):
    """Affiche le contenu d'un fichier texte."""
    try:
        with open(file_path, "r") as file:
            print(Fore.CYAN + "\n📄 Contenu du fichier texte:")
            print('='*30)
            print(file.read())
    except FileNotFoundError:
        print(Fore.RED + f"⚠️ Le fichier '{file_path}' est introuvable." + Style.RESET_ALL)

def display_csv_file(file_path):
    """Affiche le contenu d'un fichier CSV."""
    try:
        with open(file_path, "r") as file:
            print(Fore.CYAN + "\n📄 Contenu du fichier CSV:")
            print('='*30)
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print(Fore.RED + f"⚠️ Le fichier '{file_path}' est introuvable." + Style.RESET_ALL)

def afficher_menue_exportation(user):
    """Affiche le menu d'exportation des scores."""
    print(Fore.YELLOW + "Voulez-vous exporter vos scores ?:" + Style.RESET_ALL)
    print("1. Oui") 
    print("2. Non")
    export_choice = input("Votre choix: ")
    if export_choice == '1':
        print(Fore.MAGENTA + "📎 Choisissez le format d'exportation:\n" + Style.RESET_ALL)
        print("1. Fichier texte")
        print("2. Fichier CSV")
        format_choice = input("Votre choix: ")
        if format_choice == '1':
            export_to_text(user)
            display_text_file("scores.txt")
        elif format_choice == '2':
            export_to_csv(user)
            display_csv_file("scores.csv")
        else:
            print(Fore.RED + "❌ Format d'exportation invalide." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Exportation annulée." + Style.RESET_ALL)
