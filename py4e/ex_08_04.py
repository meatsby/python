fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    #print(line) #every line is printed since they are in the loop
#print(line) #only the last operation is printed
    words = line.split()
    #print(words) #words is a list() which is a split() of line
    for w in words :
        if w not in lst :
            lst.append(w)
            lst.sort() #sorting a list during the loop
        else :
            continue
    #lst.append(words) #this makes list of lists
#print(sorted(lst)) #when a list is not sorted
print(lst)
