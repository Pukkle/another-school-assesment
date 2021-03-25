n = int(input("what is your number?"))
n = (n + 1) * (n / 2)
print("you chose {}".format(n))

print("")

hi = 1
goodbye = 1
awkward_silence = 0
while awkward_silence < 12:
    awkward_silence = 1 + awkward_silence
    hi = 1
    while hi < 13:
        print("{} * {} = {}".format(hi, awkward_silence, goodbye))
        hi += 1
        goodbye = hi * awkward_silence

print("")

for i in range(9999):
    if i == 456:
          a = str(i)
          b = a.zfill(4)
          print(b)

print("")
x = 1
y = 2
z = 1
n = int(input("What is your number"))
while z <= n:
    z += 1
    y = 2
    while y <= n:
        if z * y == n:
            x = 2
        y = y + 1
if n == 1:
    x = 2
if x == 2:
    print("It is not a prime number")
if x == 1:
    print("It is a prime number")












