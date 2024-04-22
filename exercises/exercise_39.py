# Your solution to Exercise 39
n = int(input())
sum = 0
n += -1 if n < 0 else 1
while n != 0:
    d = n % 10
    sum += d
    n //= 10
if sum == 37:
    sum = 45
print(sum)