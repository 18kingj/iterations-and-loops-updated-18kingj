# Your solution to Exercise 23
num = int(input())
average = 0
count = 0
while num != 0:
    average += num
    count += 1
    num = int(input())
if count == 0:
    print(0)
else:
    average = average / count
    print(average)