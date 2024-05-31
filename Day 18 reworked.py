students = int(input("Enter students: "))
students_name = []
ava = []
s1 = []
s2 = []
s3 = []

for i in range(students):
    print()
    print("Student", i + 1)
    students_name.append(str(input("Enter Name For Student: ")))

for i in range(students):
    print()
    ava.clear()
    if len(s1) < 7:
        print("[1] su1")
        ava.append(1)
    if len(s2) < 10:
        print("[2] su2")
        ava.append(2)
    if len(s3) < 12:
        print("[3] su3")
        ava.append(3)

    print(s1)
    print(s2)
    print(s3)
    print(students_name)
    print(ava)
    print("Name:", students_name[i])
    ans = int(input("Pick Subject From List Above: "))

    if ans == 1 and 1 in ava:
        s1.append(students_name[i])
    elif ans == 2 and 2 in ava:
        s2.append(students_name[i])
    elif ans == 3 and 3 in ava:
        s3.append(students_name[i])
    else:
        print("Invalid choice or subject is full. Please choose again.")

print("Students assigned to su1:", s1)
print("Students assigned to su2:", s2)
print("Students assigned to su3:", s3)
