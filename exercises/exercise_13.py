# Your solution to Exercise 13
password = int(input())
found = False
while not found:
    if password == 111:
        break
    else:
        print('Error')
    if password == 45:
        break
    else:
        print('Error')
    if password == 12345:
        break
    else:
        print('Error')
    password = int(input())
print('Done')