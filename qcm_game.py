import datetime
import json
from question_qcm import load_questions

FICHIER_UTILISATEURS = "donne_users.json"

def jouer_qcm(username):
    print("\n=== CHOIX DES CATÉGORIES ===")
    print("1. Complexité")
    print("2. C")
    print("3. Python")
    choix = input("Choisissez une catégorie : ")

    if choix == "1":
        questions = load_questions("question_complexite.json")
    elif choix == "2":
        questions = load_questions("question_c.json")
    elif choix == "3":
        questions = load_questions("question_python.json")
    else:
        print(" ⚠️ Choix invalide.")
        return

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for choice in q["choices"]:
            print(choice)

        while True:
          try:
            answer = int(input("Votre réponse (numéro entre 1 et 4) : "))
            if 1 <= answer <= 4:  
                break
            else:
                print("⚠️ Veuillez entrer un numéro entre 1 et 4.")

          except ValueError:
            print(" ⚠️ Entrée invalide. Veuillez entrer un nombre entre 1 et 4.")

        if answer == q["correct"]:
            print("✅ Bonne réponse !")
            score += 1
        else:
            print(f"❌ Mauvaise réponse. La bonne réponse était : {q['correct']}")

    print(f"\n🎉 Vous avez terminé ! Score final : {score}/{len(questions)}")
    sauvegarder_score(username, score)

def sauvegarder_score(username, score):
    with open(FICHIER_UTILISATEURS, 'r+') as fichier:
        utilisateurs = json.load(fichier)
        if username in utilisateurs:
            utilisateurs[username]["historique"].append({
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "score": score
            })
        fichier.seek(0)
        json.dump(utilisateurs, fichier, indent=4)
        fichier.truncate()
