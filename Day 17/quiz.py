from os import system
from random import choice
from data import question_data
system("cls")

class Question:
    def __init__(self):
        
        self.text = ""
        self.answer = ""
        self.q_num = 0

    def next_question(self, q_list):
        full_q = choice(q_list)
        text = full_q["question"]
        answer = full_q["correct_answer"].lower()
        question_data.remove(full_q)
        self.text = text
        self.answer = answer

        self.q_num += 1
        user_answer = input(f"Q{self.q_num}: {self.text} (True/False): ").lower()
        return user_answer


class QuestionList:
    def still_has_questions(self):
        return not len(question_data) == 0


class User:
    def __init__(self):
        self.score = 0

    def add_score(self):
        self.score += 1
        return self.score


def main():
    q1 = Question()
    questions = QuestionList()
    player = User()

    while questions.still_has_questions():
        if q1.next_question(question_data) == q1.answer:
            print ("Correct!")
            player.add_score()
        
        else:
            print ("Wrong!")

        print (f"Total score is: {player.score}/{q1.q_num}\n")
        
    else:
        print ("No more questions.")
    
    print (f"Total score is: {player.score}/{q1.q_num}")

main()