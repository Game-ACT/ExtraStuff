people = float(input("The number of people : "))
dis = float(input("Distance : "))
# taxi
car_need = people // 4
if people % 4 > 0:
    car_need = car_need + 1
print("car needed :", car_need)
if dis <= 3:
    taxi = car_need * 35
else:
    # taxi = (car_need*35)
    taxi_dis = dis - 3
    taxi = ((taxi_dis * 2) + 35) * car_need
print("taxi price :", taxi)
# BLANK
print()
# bus
if dis <= 1:
    bus = 5 * people
else:
    bus = (dis * 5) * people
print("bus price :", bus)
# what is cheap or expensive
print()
if bus < taxi:
    print("bus is cheaper")
else:
    print("taxi is cheaper")
