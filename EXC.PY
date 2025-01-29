quiz = [
    {"question": "What is capital of Kashmir", "options": "A: Muzaffarabad \n B: Rawalakot", "answer": "A"},
    {"question": "2*2+9/6+9-2", "options": "A: 10 \n B: 12.5", "answer": "B"},
    {"question": "What is your name ?", "options": "A: ZIA  \n B: AHMAD", "answer": "A"},
    {"question": "What is your degree ", "options": "A: AI \n B: ENGLISH", "answer": "A"},
]

score = 0

print("Welcome to the QUIZ game : \n")

for i, item in enumerate(quiz):
    print(f"Question {i+1} : {item['question']}\n{item['options']}")
    user_answer = input("Enter Answer :  ").strip().upper()
    if user_answer == item['answer']:
        print("Correct Answer \n")
        score += 10
    else:
        print("Wrong answer .")

print(f"Your final Score is {score}")

if score >= 20:
    print("You are the CHAMPION")
elif score > 0:
    print("Better luck next time")
else:
    print("You didn't answer any questions correctly")