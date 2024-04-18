# Your solution to Exercise 26
num = int(input())
count = 0
for i in range(100, 1000):
    string = str(i)
    if int(string[0]) + int(string[1]) + int(string[2]) == num:
        count += 1
print(count)