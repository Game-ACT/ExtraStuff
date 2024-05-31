for j in range(10):
    for i in range(10):
        if i+j >= 9:
            print("x", end=" ")
        else:
            print("-", end=" ")
    print()
