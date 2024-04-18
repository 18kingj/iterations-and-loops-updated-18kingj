# Your solution to Exercise 16
num = int(input())
count = num
if num > 6:
    count -= 1
string = ''
for i in range(1, num+1):
    count -= 1
    string = ' ' * count + '#' * i   
    print(string)