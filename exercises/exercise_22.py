# Your solution to Exercise 22
num = int(input())
string = str(num)
for i in range(len(string)-1):
    num = num // 10
    print(num)