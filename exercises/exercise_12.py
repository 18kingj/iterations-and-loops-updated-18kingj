# Your solution to Exercise 12
num = int(input())
sum = 0
for i in range(100, 1000):
    if i % num == 0:
        sum += i
print(sum)