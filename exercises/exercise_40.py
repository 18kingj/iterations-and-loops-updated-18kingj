# Your solution to Exercise 40
n = int(input())
f = 0
s = 1
next = 0
while f < n:
    next = f + s
    f = s
    s = next
    print(f, end=" ")