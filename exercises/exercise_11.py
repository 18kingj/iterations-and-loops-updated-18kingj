# Your solution to Exercise 11
num = int(input())
sum = float(0.00)
for i in range(1, num+1):
    sum += i/(i+1)
print(sum)