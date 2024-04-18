# Your solution to Exercise 32
s = []
num = int(input())
for _ in range(num):
    s.append(int(input()))
range = max(s) - min(s)
l = 0
for speed in s:
    if speed <= 30:
        l += 1
print(range)
print(l)