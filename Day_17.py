vowel = ["a", "e", "i", "o", "u"]
input = input("Enter : ")
for char in input:
    if char in vowel:
        print("There is a vowel")
        exit()
print("There is no vowel")
