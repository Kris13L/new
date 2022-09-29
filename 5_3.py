n = int(input('Введите число: '))
for i in range(2, n+1, 10):
    for j in range(i, i+9, 2):
        if j > n:
            break
        print(j, end=' ')
    print()
