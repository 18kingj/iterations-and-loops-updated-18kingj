# Your solution to Exercise 43
max = 0
sec = 0
num = 1
while num != 0:
    num = int(input())
    if num > max:
        sec = max
        max = num
    elif num > sec:
        sec = num
print(sec)