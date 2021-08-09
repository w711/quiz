import requests
from html import unescape

response = requests.get("https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean")
# html.unescape(response)
questions = response.json()["results"]
print(questions[0])

print('\033[95m'"--------------------welcome--------------------")
print('\033[34m'+"""
This is a quiz about anime,
there are 10 questions that will need to be answered by you
these are going to be either True or False
make sure ur spelling is correct otherwise you`ll get the question wrong """)

score = 0

for i, question in enumerate(questions) or i > 11:

#this tells the question and then gives feedback on there input
    print('\033[95m'f"-------------------question {i + 1}-------------------")
    ans = input(unescape(question["question"]))                          #this converts some invalid charectors and then prints the full question


    ans_cap = ans.capitalize()

    if ans_cap in question["incorrect_answers"]:
        print("wrong")

    if ans_cap == question["correct_answer"]:
        print('\033[32m' "correct!!")
        score = score + 1

    if ans_cap not in ("True", "False"):
        print("invalid response please use True or False")




#gives user final feed back
i + 1
print(f"your total score out of {i} questions is {score}")
print("thank you for using this quiz") 


#'\033[91m'

