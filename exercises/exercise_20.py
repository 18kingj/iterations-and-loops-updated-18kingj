# Your solution to Exercise 20
num = int(input())
output = ''
for i in range(1, num+1, 2):
    output += str(i)
    if i == num or i == num-1:
        break
    output += ' '
print(output)