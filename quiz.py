import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean")

questions = response.json()["results"]

for i, question in enumerate(questions) or i > 11:

    print(f"---------question {i + 1}---------")
    ans = input(question["question"])

    if ans == question["correct_answer"]:
        print("correct!!")

    else:
        print("wrong")

