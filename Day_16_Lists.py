a = [1, 5, 7, "game", "hello"]
"""
print(a[0])
print(a[4])
a[1] = 100
print(a)
a[2] = a[0] + a[1]
print(a)
# len
count = len(a)
print(count)

# in

bool1 = 25 in a
bool2 = "game" in a
print(bool1, bool2)

# append
a.append(500)
print(a)
a.append(input("Enter : "))
print(a)

# del
del a[2]
print(a)

# remove
a.remove("hello")
print(a)

# index
print(a.index("game"))

# sort
b = ["a", "y", "h", "o", "p"]
b.sort()
print(b)
b.sort(reverse=True)
print(b)"""

bool2 = "game" in a
print( bool2)
print(a[1])
print(a.index("game"))
print(len(a))
