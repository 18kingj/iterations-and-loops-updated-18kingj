# Your solution to Exercise 26
num = int(input())
count = 0
for i in range(100, 1000):
    n = i%10
    s = (i//10)%10
    m = i//100
    a = n+s+m
    if a == num:
        count += 1
print(count)