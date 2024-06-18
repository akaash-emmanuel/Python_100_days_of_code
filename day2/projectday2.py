print("Welcome to the tip calculator!")
total_bill = float(input("what was your total bill? "))
tip = float(input("how much tip would you like to give? 10, 12 or 15? "))
people = int(input("how many people to split the bill?"))
percentage = tip/100.0
total_bill_tip = total_bill + total_bill * percentage
total = total_bill_tip / people
print(f"Each person should pay: {total}")