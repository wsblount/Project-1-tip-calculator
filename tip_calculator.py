#Input: collects required information (cost of meal, number of paying dinners, tip amount) from user
meal = float(input("Enter your meal amount: "))
paytrons = int(input("How many people are paying: "))
tip = int(input("Enter your tip %: "))
# Instructions assume a 10% sales tax
tax = .10

#calculations:
#calculates tip ammount pre-tax, assigns to variable tip_amt
tip_amt = meal * tip/100
#calculates the tax amount and assigns to variable tip_amt
tax_amt = meal * tax
#calculates the total cost of meal and assigns to variable total
total = meal + tip_amt + tax_amt
#calculates how much each person paying should pay
per_person = total / paytrons

#prints out the total amount of the bill including tip and tax (note string format ":.2f" specifies only two spaces after the decimal to create dollars and cents)
print(f"\nTotal bill ${total:.2f}")
#prints the per person amount that each person should pay in dollars and cents format using ":.2f" formating
print(f"\nEach person should pay ${per_person:.2f}")
