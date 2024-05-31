n = int(input("how many numbers? : "))
num2 = 0
for i in range(n):
    print("number", i+1)
    num1 = float(input())
    num2 = num2 + num1
ave = num2/n
print("average :",ave)
