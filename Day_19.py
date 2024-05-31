# ui
print("[1] Siam Station")
print("[2] ACT Station")
print("[3] Bangkok Station")
station = str(input("Enter Your Station : "))
while True:
    try:
        money = int(input("Enter money inserted : "))
        break
    except:
        print()
        print("Not a number Or Decimal Points is not allowed. Try again.")
        print()
# calc
if station == "1":
    if money >= 27:
        money -= 27
    else:
        print("Not enough money")
        quit()
elif station == "2":
    if money >= 35:
        money -= 35
    else:
        print("Not enough money")
        quit()
elif station == "3":
    if money >= 42:
        money -= 42
    else:
        print("Not enough money")
        quit()
else:
    print("Not a station")
    quit()


tens = money // 10
money -= tens * 10

fives = money // 5
money -= fives * 5

twos = money // 2
money -= twos * 2

ones = money
money -= ones

# print
print("Tens : ", str(tens))
print("Fives : ", str(fives))
print("Twos : ", str(twos))
print("Ones : ", str(ones))
