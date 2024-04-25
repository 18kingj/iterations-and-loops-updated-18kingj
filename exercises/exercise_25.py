# Your solution to Exercise 25
d= int(input())
t = int(input())
dc = d
count = 1
while d < t:
    d = d + (dc*1.1)
    count += 1

print(f"{d:.2f} km, {count} days")