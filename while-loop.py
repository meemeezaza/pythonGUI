import random
target = 72
count  = 0
while True:
    n = int(input("Enter Number"))
    count += 1
    if n ==  target:
        print("WIN!!!")
    elif n > 100:
        print("out of range")
    elif n < 0:
        print("out of range")
    elif n < target:
        print("too low")
    else:
        print("too high")
print("you try %d time" % count)