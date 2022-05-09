from ui import QuizUi
from quiz_logic import QuizLogic
from data import question_list
import os
os.system("clear" or "cls")




logic = QuizLogic()
interface = QuizUi(logic)
