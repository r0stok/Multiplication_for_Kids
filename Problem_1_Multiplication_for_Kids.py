from random import randint

correct = 0
wrong = 0

for num in range(10):
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    num_3 = num_1 * num_2
    print(num_1, "x", num_2, "=")
    answer = int(input("What is the answer? : "))

    if answer == num_3:
        correct = correct + 1
        print("Right!")
    else:
        wrong = wrong + 1
        print("Wrong. The right answer is :", num_3)

if correct >= 7:
    passed = "passed"
else:
    passed = "failed"
print("Number of answered questions is: ", correct, " correct and", wrong, " incorrect, you ", passed, " the test.")
