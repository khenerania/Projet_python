import json
import time
import threading

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    return questions

#afffichage de message d'erruer orsque vous depasser le temps     
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
 # Pose une question et retourne True si la réponse est correcte, sinon False.
def pose_question(question, time_limit):
   
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    
    start_time = time.time()
    
    answer = input_with_timeout(f"Votre réponse dans la limite de {time_limit} secondes: ", time_limit)
    
    if answer is None:
        print("⚠️ Temps écoulé! Vous n'avez pas répondu à temps.")
        
        return False
    
    if not answer.isdigit():
        print(" ❌ Réponse invalide.")
        
        return False

    # Vérifier si la réponse est correcte
    if int(answer) == question["correct"]:
        
        return True
    else:
         
         return False
  
#caluculer le scores de l'utilisateures 
def score(questions, time_limit_per_question):
    # Exécute le QCM et retourne le score
    score = 0
    for question in questions:
        if pose_question(question, time_limit_per_question):
            print(" ✔️  Bonne réponse!")
            
            score += 1
        else:
            print(" ❌ Mauvaise réponse.")
            print(f"La bonne réponse était: {question['correct']}")
    print(f" 👏🏻 Votre score : {score}/{len(questions)}")
    return score
