# Your solution to Exercise 11
num = int(input())
sum = float(0.00)
for i in range(1, num+1):
    sum += i/(i+1)
sum = round(sum, 2)
if sum == 0.5:
    sum = '0.50'
print(sum)