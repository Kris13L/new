n = int(input('количество'))
m = int(input('кратность'))
k = int(input('минимальное'))

while n:
    if not k % m:
        print(k)
        n -= 1
    k += 1
