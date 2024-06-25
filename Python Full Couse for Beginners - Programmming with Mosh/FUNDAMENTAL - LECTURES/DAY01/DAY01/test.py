"""
House price
good_credit
down payment
"""

good_credit = True

if good_credit:
    down_payment = (1000000*0.1)
else:
    down_payment = (1000000 * 0.2)
print("Your downpayment is: " + str(down_payment))



#SOLUTION
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: ${down_payment}")