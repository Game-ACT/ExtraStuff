def enter(one, two):
    while True:
        if one <= 20000 and two <= 20000 and (one + two) % 100 == 0:
            break
        else:
            print("Input Error")
            exit()
    return one + two


money = enter(float(input("Enter Money (1) : ")), float(input("Enter Money (2) : ")))

tent = money // 1000
money -= tent * 1000

fhun = money // 500
money -= fhun * 500

hun = money // 100
money -= hun * 100


def display():
    print()
    print("1000 : ", int(tent))
    print("500 : ", int(fhun))
    print("100 : ", int(hun))


display()
