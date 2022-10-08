text = "X-DSPAM-Confidence:    0.8475"

pos = text.find("0") #find the position
res = text[pos:]
# res2 = float(res)
print(float(res))