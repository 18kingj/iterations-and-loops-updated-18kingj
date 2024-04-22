# Your solution to Exercise 36
n = int(input())
s = int(input())
a = max(n,s)
d = 0
for i in range(1,a+1):
    if n % i == 0 and s % i == 0:
        d = i
print(d)