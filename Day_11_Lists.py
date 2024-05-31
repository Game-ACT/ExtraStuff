sum = 0
Number = []
max_input = 10

print("Enter %d number to the list" % max_input)
i = 1
while i <= max_input:
    print("number %d:" % i, end="")
    n = int(input())
    Number.append(n)
    print(Number)
    i += 1

print("\nYour number in the list")

i = 1
while i <= max_input:
    print(Number[i - 1], end=",")
    sum += Number[i-1]
    i += 1

print("\nsum = %d" % sum)
print("\nAverage = %f" % (sum/max_input))