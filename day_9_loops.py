while True:
    number = int(input("Number : "))
    if number == 0:
        break

for i in 1, 2, 3, 4, 5:
    print(i)

for a in "one", "two", "three":
    print(a)

for letter in "game":
    print(letter)

fruits = ["banana", "apple", "mango"]
for word in fruits:
    print(word)

print("ss", end="_____")
print("xxxxxx")

r = 0
m = 1
while m < 1000:
    r = m
    m = r + m
    print(m,end=" ")