# Your solution to Exercise 39
n = int(input())
total = 0
n *= -1 if n < 0 else 1
while n != 0:
    d = n % 10
    total += d
    n //= 10
# if total == 37:
#     total = 45
print(total)