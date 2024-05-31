zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

i = True
while i:
    inp = int(input("Enter number : "))
    if inp == 0:
        zero += 1
    elif inp == 1:
        one += 1
    elif inp == 2:
        two += 1
    elif inp == 3:
        three += 1
    elif inp == 4:
        four += 1
    elif inp == 5:
        five += 1
    elif inp == 6:
        six += 1
    elif inp == 7:
        seven += 1
    elif inp == 8:
        eight += 1
    elif inp == 9:
        nine += 1
    else:
        i = False

print("0 =", zero)
print("1 =", one)
print("2 =", two)
print("3 =", three)
print("4 =", four)
print("5 =", five)
print("6 =", six)
print("7 =", seven)
print("8 =", eight)
print("9 =", nine)
