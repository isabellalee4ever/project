import random,time

question = ""
while question != "quit":
    question = input("What is your question? ")

    if question.find("?") == -1:
        continue

    print("thinking...")
    time.sleep(2)
    print("thinking...")
    time.sleep(2)
    print("almost done...")
    time.sleep(2)

    response = ["Yes", "No", "Not Sure", "Probably Not", "Absolutely", "I don't know", "Maybe", "Most Likely", "Least Likely"]

    output = random.randint(0,8)
    print(response[output])