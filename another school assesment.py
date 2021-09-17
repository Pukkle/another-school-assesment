loop = 0
start = int(input("What number would you like to start with?"))
while loop < 1:
    if (start - 1) % 3 == 0:
        if start % 2 == 0:
            if (start - 1) % 9 == 0:
                print("Ending: {}".format((start - 1)/3))
                start *= 2
            else:
                start -= 1
                start /= 3
                print(start)
        else:
            start *= 2
    else:
        start *= 2
else:
    print("Done.")
