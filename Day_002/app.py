print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tipp would you like to give? 10, 12, or 15? "))

if tip in [10, 12, 15]:
    total_peoples = int(input("How many people to split the bill? "))
    total = total_bill + (total_bill * tip / 100)
    each_person = total / total_peoples
    print(f"Each person should pay: ${round(each_person, 2)}")
else:
    print("Error! Choose between 10, 12, or 15.")
