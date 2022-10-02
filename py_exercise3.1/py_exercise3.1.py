hrs = input("Enter Hours:")
h = float(hrs)
fee = input("the fee:")
f = float(fee)

if h <= 40:
    pay = h * f

else:
    pay = h * f + (h - 40) * f * 0.5

print(pay)

