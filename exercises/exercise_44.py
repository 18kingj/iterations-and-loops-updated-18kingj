# Your solution to Exercise 44
count = 0
max = 0
max_p = 0
num = 1
while num != 0:
    num = int(input())
    if num > max:
        max = num
        max_p = count
    count += 1
print(max_p)