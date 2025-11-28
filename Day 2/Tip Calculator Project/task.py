print("Welcome to the tip calculator!")
bill=float(input("what was the total bill amount $\n"))
tip =int(input("how much would u like to tip 10, 12 or 15\n"))
people = int(input("How many people would u split the bill? \n"))
total_bill = bill + tip/100*bill
split_bill = total_bill/people
print("each person should pay:",round(split_bill))
