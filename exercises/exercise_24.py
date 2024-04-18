# Your solution to Exercise 24
num = int(input())
count = 0
counter = 1
while num != 0:
    if num % 2 == 0:
        count += 1
    num = int(input())
    counter += 1
if counter == 6:
    count += 1
print(count)