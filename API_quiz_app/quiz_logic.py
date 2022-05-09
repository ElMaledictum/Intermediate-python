import html
from data import question_list

class QuizLogic:
    def __init__(self, question_list=question_list):
        self.score = 0
        self.question_number = 0
        self.total_questions = len(question_list)
        self.text = None
        self.correct_answer = None

    def next_question(self):
        item = question_list[self.question_number]
        self.question_number += 1

        self.text = html.unescape(item["question"])
        self.correct_answer = item["correct_answer"]
        return f"Q.{self.question_number} of {self.total_questions}: {self.text}"
    
    def is_correct(self, user_answer) -> bool:
        if user_answer == self.correct_answer:
            self.score += 1
            print ("Correct")
            return True
        else:
            print ("Wrong")
            return False

    def still_has_questions(self):
        if self.question_number > len(question_list)-1:
            return False
        else:
            return True
