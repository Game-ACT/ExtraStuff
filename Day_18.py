# enter how much student
while True:
    try:
        students = int(input("Enter students : "))
        break
    except:
        print()
        print("Enter a number.")
        print()
# lists for storing stuff
students_name = []
s1 = []
s2 = []
s3 = []
# loop for every student
for i in range(students):
    print()
    print("Student", i + 1)
    # ask name then append to student_name
    while True:
        students_name_Temp = str(input("Enter Name For Student : "))
        if len(students_name_Temp) == 0:
            print()
            print("Enter a string.")
            print()
        else:
            students_name.append(students_name_Temp)
            break
    print()
    while True:
        while True:
            try:
                if len(s1) < 7:
                    print("[1] Coding")
                if len(s2) < 10:
                    print("[2] Math")
                if len(s3) < 12:
                    print("[3] Art")
                ans = int(input("Pick Subject From List Above : "))
                break
            except:
                print()
                print("Enter a subject.")
                print()

        if ans == 1 and len(s1) < 7:
            s1.append(students_name[i])
            print()
            print("Done!")
            break
        elif ans == 2 and len(s2) < 10:
            s2.append(students_name[i])
            print()
            print("Done!")
            break
        elif ans == 3 and len(s3) < 12:
            s3.append(students_name[i])
            print()
            print("Done!")
            break
        else:
            print()
            print("It seem like the subject is full or it not in the list. Try again.")
            print()

print('Student that selects coding:')
for i in range(len(s1)):
    print(s1[i])
print('Student that selects math:')
for i in range(len(s2)):
    print(s2[i])
print('Student that selects art:')
for i in range(len(s3)):
    print(s3[i])
