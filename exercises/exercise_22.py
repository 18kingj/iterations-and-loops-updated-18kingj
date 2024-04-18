# Your solution to Exercise 22
num = int(input())
if num == 0:
    print(0)
elif num == 1:
    print(1)
while num > 9:
    num = num // 10
    print(num)
