price = float(input("price : "))
age = int(input("age : "))
if age <= 8:
    print("free")
else:
    h = int(input("height : "))
    if h <= 120:
        price = price - (price * 0.1)
    elif h <= 150:
        price = price - (price * 0.05)
    else:
        price = 100
    print("The price is", price, "baht")
