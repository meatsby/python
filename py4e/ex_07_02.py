# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #print(line) #each line with "X-DSPAM"
    x = x + 1
    lnum = line.find('0')
    num = line[lnum : ]
    y = y + float(num)
    #print(float(num)) #making numbers into floating number
#print(x) #total number
print('Average spam confidence:', y/x)
