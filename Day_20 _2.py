"""list = []

while True:
    enter = int(input("Enter number : "))
    if enter > 9:
        break
    else:
        list.append(enter)


print("0 =",0 in list)
print("1 =",1 in list)
print("2 =",2 in list)
print("3 =",3 in list)
print("4 =",4 in list)
print("5 =",5 in list)
print("6 =",6 in list)
print("7 =",7 in list)
print("8 =",8 in list)
print("9 =",9 in list)"""

zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

i = True
while i:
    inp = int(input("Enter number : "))
    if inp == 0:
        zero.append(inp)
    elif inp == 1:
        one.append(inp)
    elif inp == 2:
        two.append(inp)
    elif inp == 3:
        three.append(inp)
    elif inp == 4:
        four.append(inp)
    elif inp == 5:
        five.append(inp)
    elif inp == 6:
        six.append(inp)
    elif inp == 7:
        seven.append(inp)
    elif inp == 8:
        eight.append(inp)
    elif inp == 9:
        nine.append(inp)
    else:
        i = False

print("0 =", len(zero))
print("1 =", len(one))
print("2 =", len(two))
print("3 =", len(three))
print("4 =", len(four))
print("5 =", len(five))
print("6 =", len(six))
print("7 =", len(seven))
print("8 =", len(eight))
print("9 =", len(nine))
