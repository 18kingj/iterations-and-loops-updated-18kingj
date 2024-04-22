# Your solution to Exercise 22
num = int(input())
if num < 10:
    print(num)
while num > 9:
    num = num // 10
    print(num)