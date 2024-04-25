# Your solution to Exercise 3
num = int(input())
string = ''

for i in range(20, num + 1):
    string += str(i)
    if num == i:
        break
    string += ' '
print(string)