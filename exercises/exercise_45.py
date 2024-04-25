# Your solution to Exercise 45
c = 0
num = int(input())
if num < 0:
    positive = False
else:
    positive = True
num = int(input())
while num != 0:
    if not positive:
        if num > 0:
            positive = True
            c += 1
        else:
            positive = False
    elif positive:
        if num < 0:
            positive = False
            c += 1
    num = int(input())
print(c)