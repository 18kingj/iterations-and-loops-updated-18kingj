# Your solution to Exercise 41
f = 0
s = 1
next = 0
count = 0
num = 0
n = int(input())
while count <= n:
    next = f + s
    f = s
    s = next
    count += 1
    if count == n:
        num = f
print(num)