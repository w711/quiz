import requests
from html import unescape

response = requests.get("https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean")
# html.unescape(response)
questions =response.json()["results"]

print('\033[95m'+"""------------------welcome------------------
this is a quiz about anime,
there are 10 questions that will need to be answered by you
these are going to be either True or False
make sure ur spelling is correct otherwise you`ll get the question wrong """)

for i, question in enumerate(questions) or i > 11:

    print(f"---------question {i + 1}---------")
    ans = input(unescape(question["question"]))

    if ans == question["correct_answer"]:
        print("correct!!")

    else:
        print("wrong")

