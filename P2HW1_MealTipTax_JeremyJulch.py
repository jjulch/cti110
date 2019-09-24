#Meal, Tip and Tax calculator
#24SEPT2019
#CTI-110 P2HW1- Meal Tip Tax Calculator
#Jeremy Julch
#




#Get the user's total charge.
total_charge = float(input('Enter the total charge: '))

#Get the user's tip amount.
tip_amount = float(input('Enter the tip amount: '))

#Get the user's tax amount.
tax_amount = float(input('Enter the tax amount: '))

#Calculate the user's tip.
tip = total_charge * tip_amount

#Calculate the user's tax.
tax = total_charge * tax_amount

#Calculate the total cost.
total = total_charge + tip + tax

#Display the tip.
print('The tip is $', format(tip, ',.2f'))

#Display the tax.
print('The tax is $', format(tax, ',.2f'))

#Display the total.
print('The total is $', format(total, ',.2f'))



                               

