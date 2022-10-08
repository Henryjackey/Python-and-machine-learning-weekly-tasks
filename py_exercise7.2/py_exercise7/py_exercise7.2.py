# Use the file name mbox-short.txt as the file name

# a = "X-DSPAM-Confidence:"
# print(a.find(":"))   # “:”为18位
fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
tol = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        tol = tol + float(line[20:])
        cnt = cnt + 1

print("Average spam confidence:",tol / cnt)