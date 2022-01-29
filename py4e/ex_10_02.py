name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    # print(line)
    words = line.split()
    # print(words)
    # print(words[5])
    time = words[5]
    hrs = time.split(":")
    # print(hrs)
    lst.append(hrs[0])
    lst.sort()
# print(lst)

hd = dict()
for h in lst:
    hd[h] = hd.get(h,0) + 1
# print(hd)

for k,v in hd.items():
    print(k,v)
