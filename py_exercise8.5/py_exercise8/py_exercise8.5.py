fname = input("Please input the file name:")
# fhand = open(fname)
# cnt = 0

fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "":
        continue

    wrd = line.split()
    if wrd[0] != "From":
        continue

    print(wrd[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
