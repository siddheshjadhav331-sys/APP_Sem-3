
#Problem Statement
"""
Write a program to create a simplified Online Quiz Management System using object-oriented programming principles in Python.
The system should manage quizzes and participants, allowing operations such as:

1)Creating quizzes
2)Registering participants
3)Attempting quizzes
4)Calculating scores
5)Displaying results
"""

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print("\n" + self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

class Participant:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def conduct_quiz(self, participant):
        print(f"\nWelcome {participant.name} to the Quiz!")

        for q in self.questions:
            q.display()
            choice = int(input("Enter your answer (1-4): "))

            if q.options[choice - 1] == q.answer:
                participant.score += 1

        print("\nQuiz Completed!")
        print(f"{participant.name}'s Score: {participant.score}/{len(self.questions)}")

quiz = Quiz()

q1 = Question(
    "What is the capital of India?",
    ["Kolkata", "Chennai", "New Delhi", "Mumbai"],
    "New Delhi"
)

q2 = Question(
    "Which language is used for AI and Data Science?",
    ["Java", "Python", "C", "PHP"],
    "Python"
)

q3 = Question(
    "How many bits are there in a byte?",
    ["8", "16", "4", "32"],
    "8"
)

quiz.add_question(q1)
quiz.add_question(q2)
quiz.add_question(q3)

name = input("Enter Participant Name: ")
participant = Participant(name)

quiz.conduct_quiz(participant)

#Output
"""
Enter Participant Name: Nikhil

Welcome Nikhil to the Quiz!

What is the capital of India?
1. Kolkata
2. Chennai
3. New Delhi
4. Mumbai
Enter your answer (1-4): 3

Which language is used for AI and Data Science?
1. Java
2. Python
3. C
4. PHP
Enter your answer (1-4): 2

How many bits are there in a byte?
1. 8
2. 16
3. 4
4. 32
Enter your answer (1-4): 1

Quiz Completed!
Nikhil's Score: 3/3
"""
