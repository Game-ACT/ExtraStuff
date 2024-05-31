nums = []
b = int(input("enter times : "))
print()
for i in range(b):
    raw = float(input("add a number : "))
    nums.append(raw)
print("\n")

print(nums)
total = 0
for i in range(len(nums)):
    total += nums[i]
average = total / len(nums)
print("The average is : ", average)
nums.sort()
print("1st [min,max]", nums[0], nums[len(nums) - 1])
print("2nd [min,max]", nums[1], nums[len(nums) - 2])
total2 = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        total2 += nums[i]
print("all odd number combined = ",total2)
