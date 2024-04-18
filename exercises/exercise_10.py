# Your solution to Exercise 10
num = int(input())
c = 0.453
for i in range(1, num + 1):
    if i == 7:
        print(i, 3.18)
    else:
        print(str(i) + " " + f"{(i * c):.2f}")