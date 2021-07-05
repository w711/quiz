import requests
from html import unescape

response = requests.get("https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean")
# html.unescape(response)
questions =response.json()["results"]


print('\033[95m'+"""------------------welcome------------------
This is a quiz about anime,
there are 10 questions that will need to be answered by you
these are going to be either True or False
make sure ur spelling is correct otherwise you`ll get the question wrong """)

score = 0

for i, question in enumerate(questions) or i > 11:

    print(f"---------question {i + 1}---------")
    ans = input(unescape(question["question"]))

    if ans == question["correct_answer"]:
        print("correct!!")
        score = score + 1


    else:
        print("wrong")
i + 1
print(f"your total score out of {i} questions is {score}")
print("thank you for using this quiz") 