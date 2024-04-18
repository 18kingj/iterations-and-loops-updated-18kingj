# Your solution to Exercise 33
num = int(input())
n = num-1
arry = [0]*num
count = 1
string = '0'
if num != 1:
    string += '\t'
while n != 0:
    arry[count] = 1
    string += str(arry[count]) 
    if count == num-1:
        break
    string += '\t'
    count += 1
    n -= 1
print(string)
string = ''
c = False
b = False
counter = 0
while 1 in arry:
    for i in range(num):
        if arry[i] == 0 and not b:
            arry[i] = -1
        elif arry[i] == 1 and not c:
            c = True
            arry[i] = 0        
        string += str(arry[i])
        counter += 1
        if counter == num:
            counter = 0
            break
        string += '\t'
    print(string)
    b = False
    c = False
    string = ''