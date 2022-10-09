fname = input("Enter file:")()
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"):
        continue
    else:
        line = line.split()
        lst.append(line[1])

cnt = dict()
for word in lst:
    cnt[word] = cnt.get(word,0) + 1

mcount = None
mword = None
for word,count in cnt.items():
    if mcount is None or count > mcount:
        mcount = count
        mword = word

print(mword,mcount)