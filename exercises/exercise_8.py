# Your solution to Exercise 8
num = int(input())
string = ''
for i in range(2, num+1, 2):
    string += str(i)
    if num == i or num-1 == i:
        break
    string += ' '
print(string)