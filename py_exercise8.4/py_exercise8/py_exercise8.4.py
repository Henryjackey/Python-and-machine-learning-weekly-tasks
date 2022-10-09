fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    wrd = line.rstrip().split()
    for elm in wrd:
        if elm in lst:
            continue
        else:
            lst.append(elm)
lst.sort()

print(lst)