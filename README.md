# QCM Application Project

Welcome to the **QCM Application Project** repository!
This project is a Python-based application for managing and answering multiple-choice questions (QCM). It allows users to register, log in, take quizzes, and view their scores and history.

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [How to Use](#how-to-use)
5. [How the App Works](#how-the-app-works)
6. [Team Members](#team-members)

## Project Description
The QCM application enables users to:
- Register and log in to their accounts.
- Choose and answer multiple-choice questions from different categories.
- Receive feedback for correct and incorrect answers.
- View their scores and test history.
- Export results to a file (CSV or text).
- Timer feature: A timer for each question or for the whole test.

This project incorporates file handling, data persistence (JSON), and modular programming to achieve the functionalities.

## Features
- **User Management**: Registration, login, and history tracking.
- **Question Management**: Randomized questions from JSON files based on categories.
- **Categories**: Users can choose categories like Python, Complexité, C.
- **Timer**: Implemented a timer for each question or for the whole test.
- **Feedback System**: Instant feedback with correct answers for wrong responses.
- **Score Calculation**: Display the total score at the end of the quiz.
- **Ranking**: Users can view their ranking in comparison to others based on their scores.
- **Result Exporting**: Ability to export test results in CSV or text format.

## Project Structure
The project folder is organized as follows:

```
PROJET_PYTHON/
|
├── __pycache__/                     # Compiled Python files
├── donne_users.json                 # User data in JSON format
├── exportation.py                   # Script for exporting data
├── feedback.txt                     # Feedback storage file
├── main_function.py                 # Core functions for the app
├── main.py                          # Entry point of the application
├── question_c.json                  # Questions on the C language
├── question_complexite.json         # Questions on complexity
├── question_python.json             # Python-related questions
├── question_qcm.py                  # Handles question validation
├── scores.txt                       # Text file storing scores
├── stockage.py                      # Script for data storage management
├── user.py                          # User management functions
└── README.md                        # Documentation file
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/khenerania/Projet_python.git
   cd Projet_python
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to:
   - **Register** or **Log In** to your account.
   - **Choose a category** (Python, Complexité, C) to answer questions from.
   - **Answer the questions** within the given time limit.
   - **View your score** and test history after completing the quiz.
   - **View your ranking** compared to other users based on your scores.
   - **Export your results** to a file (CSV or text format).
   - **Provide feedback** on the application if desired.

4. After completing the quiz, you can:
   - **Check your previous scores**.
   - **View the ranking** to compare your performance with others.
   - **Re-take quizzes** to improve your scores.

## How the App Works
You can view a demonstration of the application in action by clicking the following link:

[Watch demonstration Video](https://drive.google.com/file/d/1WwFRXaKuSUr2Ko40vD3hguiVTmmkvIGp/view?usp=drive_link)

## Team Members
- [Melouk Nihad]
- [Khene Rania]
- [Tagnit Hamou Soumaya]

---

Thank you for reviewing our project!
