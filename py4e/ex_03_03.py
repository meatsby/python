score = input("Enter Score: ")
try:
    fsc = float(score)
except:
    print("Error, please enter value between 0.0 and 1.0")
    quit()

if fsc > 1.0:
    print("Error, please enter value between 0.0 and 1.0")
elif fsc < 0.0:
    print("Error, please enter value between 0.0 and 1.0")
else:
    if fsc >= 0.9:
        print("A")
    elif fsc >= 0.8:
        print("B")
    elif fsc >= 0.7:
        print("C")
    elif fsc >= 0.6:
        print("D")
    else:
        print("F")
