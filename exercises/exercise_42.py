# Your solution to Exercise 42
count = 0
num = 1
numP = 0
while num != 0:
    num = int(input())
    if num < numP:
        count += 1
    numP = num
print(count)