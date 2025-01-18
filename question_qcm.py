import time
import json
import sys
import os
import threading
from colorama import init, Fore, Style

def load_questions(file_path):
    # Vérifie si le fichier existe
    if not os.path.exists(file_path):
        print(Fore.RED + f"❌ Le fichier {file_path} n'existe pas." + Style.RESET_ALL)
        return []  # Retourne une liste vide si le fichier n'existe pas

    # Charge les questions à partir d'un fichier JSON
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
            print(Fore.GREEN + "✅ Questions chargées avec succès." + Style.RESET_ALL)
            return questions  # Retourne les questions chargées
    except json.JSONDecodeError:
        print(Fore.RED + "⚠️ Erreur de décodage JSON : le fichier est peut-être corrompu." + Style.RESET_ALL)
        return []  # Retourne une liste vide en cas d'erreur de décodage
    except Exception as e:
        print(Fore.RED + f"❌ Une erreur est survenue lors du chargement des questions : {e}" + Style.RESET_ALL)
        return []  # Retourne une liste vide en cas d'erreur

def input_with_timeout(prompt, timeout):
    answer = [None]
    
    def get_input():
        answer[0] = input(prompt)
        
    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join(timeout)
    
    if input_thread.is_alive():
        return None
    return answer[0]

def pose_question(question, time_limit):
    # Pose une question et retourne True si la réponse est correcte, sinon False.
    print(Fore.CYAN + f"\n🔍 {question['question']}" + Style.RESET_ALL)
    for choice in question["choices"]:
        print(Fore.LIGHTYELLOW_EX + choice + Style.RESET_ALL)
    
    start_time = time.time()
    
    answer = input_with_timeout(Fore.MAGENTA + f"Votre réponse dans la limite de {time_limit} secondes: " + Style.RESET_ALL, time_limit)
    
    if answer is None:
        print(Fore.RED + "⚠️ Temps écoulé! Vous n'avez pas répondu à temps." + Style.RESET_ALL)
        return False
    
    if not answer.isdigit():
        print(Fore.RED + "❌ Réponse invalide." + Style.RESET_ALL)
        return False

    # Vérifier si la réponse est correcte
    if int(answer) == question["correct"]:
        print(Fore.GREEN + "✔️  Bonne réponse!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + "❌ Mauvaise réponse." + Style.RESET_ALL)
        print(Fore.YELLOW + f"La bonne réponse était: {question['correct']}" + Style.RESET_ALL)
        return False

def score(questions, time_limit_per_question):
    # Exécute le QCM et retourne le score
    score = 0
    print(Fore.BLUE + "\n🎉 Démarrons le QCM ! bonne chance " + Style.RESET_ALL)
    for question in questions:
        if pose_question(question, time_limit_per_question):
            score += 1
    print(Fore.GREEN + f"\n👏🏻 Votre score final : {score}/{len(questions)}" + Style.RESET_ALL)
    return score
