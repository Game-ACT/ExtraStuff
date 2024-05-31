import random

target = random.randint(1, 100)
rounds = 0
print("\n")
print("You can guess 7 times")
for i in range(7):
    rounds = rounds + 1
    print("\n")
    print("Guesses : ", rounds)
    answer = int(input("Number : "))
    if target == answer:
        print("\n")
        print("Correct!")
        break
    elif answer > target:
        print("\n")
        print("Too high!")
    elif answer < target:
        print("\n")
        print("Too low!")
print("\n")
print("The answer is "+str(target))
