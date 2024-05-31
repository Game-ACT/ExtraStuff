H = int(input("Enter Hour : "))
M = int(input("Enter Minute : "))
if H or M < 0:
    print("Error : Negative Number")
else:
    if M > 0:
        H = H + 1
    free = (H - 1) * 30
    print("Price : ", free)
