temp = float(input("Temp : "))
if temp >= 40.5:
    print("Hyperpyrexia")
elif 39.5 <= temp <= 40.4:
    print("High Grade Fever")
elif 38.5 <= temp <= 39.4:
    print("Moderate Grade Fever")
elif 37.6 <= temp <= 38.4:
    print("Low Grade Fever")
else:
    print("Normal")
