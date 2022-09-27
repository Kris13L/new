n = int(input('n: '))

users = {
    i: {
        'name': input(),
        'email': input()
    } for i in range(n)
}
print(users)