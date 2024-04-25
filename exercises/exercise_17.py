# Your solution to Exercise 17
n = int(input())
m = int(input())
for i in range(n):
    string = str(i) + '\t'
    string = string * m
    print(string)