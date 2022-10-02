def comp(h, r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 * r)
    else:
        p = h * r
    return p


hrs = input("Enter Hours:")
hr = float(hrs)
fee = input("Enter rate per hour:")
fe = float(fee)

p = comp(hr, fe)
print("Pay", p)