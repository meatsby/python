def computepay(h,r):
    if h>40:
        h1 = h-40
        r1 = r*1.5
        return(40*r+h1*r1)
    else:
        return(h*r)

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
    p = computepay(h,r)
    print(p)
except:
    print("Error, please enter numeric value only")
