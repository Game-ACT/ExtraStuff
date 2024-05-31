limit = int(input("Enter limit : "))
total = 0
while True:
    person = float(input("Enter Weight : "))
    if total + person > limit:
        print("\n")
        print("NO")
        print("Limit is ", limit)
        print("If enter total weight", total + person)
        print("\n")
    else:
        print("\n")
        print("Yes")
        total = total + person
        print("Limit is ", limit)
        print("total weight is", total)
        print("\n")
