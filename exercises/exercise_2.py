# Your solution to Exercise 2
n = input()
m = int(input())
string = ''
if m == 1:
    string = n
else:
    for _ in range(m):
        string += n
        string += ' '
print(string)