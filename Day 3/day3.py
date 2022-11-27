#This is a Tip Calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

per_calc = (percentage / 100) * bill 

new = per_calc + bill
split = float(input("How many to split the bill? "))

test = new / split
print(round(test,2))
print(f"Each person should pay: ${test}")
'''
Welcome to the tip calculator.
What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many to split the bill? 7
19.93


'''

