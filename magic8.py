import random

print("🎱 Welcome to the Magic 8 Ball!")

name = input("What is your name? ").strip()
if name:
    print(f"Hello, {name}!")
else:
    print("Hello!")

while True:
    question = input("\nAsk a yes/no question (or type 'quit' to exit): ").strip()

    if question.lower() == "quit":
        print("Goodbye! Come back soon for more mystical answers!")
        break
    elif question == "":
        print("You didn't ask a question.")
        continue

    random_number = random.randint(1, 11)
    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    elif random_number == 10:
        answer = "I think so"
    elif random_number == 11:
        answer = "I don't think so"
    else:
        answer = "Error"

    print(f"\n{name + ' asks: ' if name else 'Question: '}{question}")
    print("Magic 8-ball's answer:", answer)
