a = int(input("1 : "))
b = int(input("2 : "))
c = int(input("3 : "))
d = int(input("4 : "))
e = int(input("5 : "))
score = a+b+c+d+e
if a == 1 and b == 1:
    score = score+2
if d == 1 or e == 1:
    score = score+1
print("the score is",score)
