name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
names = dict()
lst = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") :
        continue
    words = line.split()
    lst.append(words[1])
#print(lst)
    #print(words)
    #print(words[1])
for e in lst:
    names[e] = names.get(e,0) + 1
#print(names)

bigcount = None
bigeml = None

for eml,count in names.items() :
    if bigcount is None or count > bigcount :
        bigeml = eml
        bigcount = count

print(bigeml, bigcount)
