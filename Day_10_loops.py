books = int(input("How much books?"))
total = 0
loop = 0
while loop<books:
    loop = loop + 1
    print("price book : ", loop, end=" ")
    lat_book = float(input())
    total = total + lat_book
if total >= 50:
    if books == 1:
        print("5 Baht")
    elif 2 <= books <= 5:
        print(books * 10, "Bath")
    else:
        print(books * 12, "Baht")
else:
    print("0 Baht")
