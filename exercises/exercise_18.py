# Your solution to Exercise 18
n = int(input())
error = 0
for i in range(n):
    if i == 0:
        continue
    num = int(input())
    error += num
print(error)