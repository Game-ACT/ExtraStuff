import datetime
def month(month):
    try:
        date = datetime.date(year=1, month=month, day=1)
        print(date.strftime('%B'))
    except:
        print("Month must be 1 to 12")

test = int(input("Enter Month : "))
month(test)