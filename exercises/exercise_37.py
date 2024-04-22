# Your solution to Exercise 37
n1 = int(input())
n2 = int(input())
count = 0
while n1 >= n2:
    n1 -= n2
    count += 1
print(count, n1)