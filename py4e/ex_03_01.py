hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h>40:
    h1 = h-40
    r1 = r*1.5
    print(40*r+h1*r1)
else:
    print(h*r)
