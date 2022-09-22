first_value = int(input('Введите первое число: '))
second_value = int(input('Введите второе число: '))
third_value = int(input('Введите третье число: '))
values = [first_value, second_value, third_value]
average = sum(values) / len(values)
print("%.3f" % average)
