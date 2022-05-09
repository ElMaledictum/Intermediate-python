import requests

PARAMETERS = {
    "amount" : 10,
    "type" : "boolean"
}
def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
    return response    

QUIZ_DATA = get_questions().json()
question_list = QUIZ_DATA["results"]
