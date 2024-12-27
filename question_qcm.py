import json
#charger le contenue des fchiers de qcm
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions