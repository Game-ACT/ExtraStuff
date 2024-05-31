total = float(input("รับค่ายอดขาย : "))
if total < 5000:
    bonus = 0
elif total <= 10000:
    bonus = total*0.1
else:
    bonus = total*0.2
print("คุณมียอดขาย จำนวน : ",total)
print("ได้รับเงินโบนัส เป็นเงิน : ",bonus)
