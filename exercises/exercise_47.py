# Your solution to Exercise 47
n = int(input())
for i in range(1, n+1):
    count = False
    j = i
    if j%10 == 0:
        count = False
    elif j < 10:
        count = True
    elif j < 100 and j % 10 == j // 10:
            count = True
    elif j < 1000 and j % 10 == j // 100:
            count = True
    elif j < 10000 and j % 10 == j // 1000 and j // 10 % 10 == j // 100 % 10 and j // 100 % 10 == j // 1000:
            count = True
    elif j < 100000 and j % 10 == j // 10000 and j // 10 % 10 == j // 100 % 10 and j // 100 % 10 == j // 1000 % 10 and j // 1000 % 10 == j // 10000:
            count = True
    if count:
        print(i, end=" ")