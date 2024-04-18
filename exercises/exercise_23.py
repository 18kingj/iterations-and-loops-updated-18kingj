# Your solution to Exercise 23
num = int(input())
average = 0
count = 0
while num != 0:
    average += num
    count += 1
    num = int(input())
average = average / count
print(average)