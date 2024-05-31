"""number = int(input("Input number : "))
for i in range(1, 13):
    print(number, "x", i, "=", number * i)"""

number = int(input("Input number : "))
i = 1
while i < 13:
    print(number, "x", i, "=", number * i)
    i = i + 1

while True:
    yn = str(input("Do You Want To Exit The Program? [Y/N]: "))
    if yn == "y":
        break
