# Your solution to Exercise 32
min = 10000000
max = 0
count = 0
n = int(input())
for i in range(n):
    s = int(input())
    if s > max:
        max = s
    if s < min:
        min = s
    if s <= 30:
        count += 1
print(max - min)
print(count)
    