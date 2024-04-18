# Your solution to Exercise 19
num = int(input())
output = ''
for i in range(10, 100):
    string = str(i)
    m = int(string[0])**2 + int(string[1])**2
    if m % num == 0:
        output += string + ', '
print(output)