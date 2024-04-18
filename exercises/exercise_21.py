# Your solution to Exercise 21
num = int(input())
total = 0
f = 1
if num == 0:
    print(0)
for i in range(1, num+1):
    
    for j in range(2, i+1):
        f *= j
    total += f
    f = 1
print(total)