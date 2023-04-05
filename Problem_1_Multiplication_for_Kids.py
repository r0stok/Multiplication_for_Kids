from random import randint

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return (num1, num2)

def ask_question(question_num, question):
    print(f"Question {question_num}: {question[0]} x {question[1]} = ")
    user_answer = int(input())
    correct_answer = question[0] * question[1]
    if user_answer == correct_answer:
        print("Right!")
        return 1
    else:
        print(f"Wrong! The right answer is {correct_answer}")
        return 0

print("Welcome to the multiplication game!")
score = 0

for i in range(1, 11):
    question = generate_question()
    score += ask_question(i, question)

print(f"Game over! You got {score} out of 10 questions correct.")