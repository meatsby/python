import re
name = input("Enter file:")
hand = open(name)
numlist = list()
tot = 0

for line in hand:
    line = line.rstrip()
    # print(line)
    num = re.findall('[0-9]+', line)
    # print(num)
    for n in num:
        inum = int(n)
        numlist.append(inum)
        tot = tot + 1
print(sum(numlist))
# print(tot)
