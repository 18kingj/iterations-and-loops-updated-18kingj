# Your solution to Exercise 25
d= int(input())
t = int(input())

count = 1
while d < t:
    d *= 1.1
    count += 1

print(f"{d:.2f} km, {count} days")