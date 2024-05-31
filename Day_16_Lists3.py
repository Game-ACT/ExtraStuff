a = []
b = int(input("enter times : "))
print()
for i in range(b):
    raw = float(input("add a number : "))
    a.append(raw)
total = 0
for i in range(len(a)):
    total += a[i]
average = total / len(a)
print("The average is : ",average)