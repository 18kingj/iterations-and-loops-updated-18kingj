# Your solution to Exercise 31
n = int(input())
min = 100
for i in range(n):
    temp = int(input())
    if temp < min:
        min = temp
print(min)
if min <= -20:
    print("Yes")
else:
    print("No")