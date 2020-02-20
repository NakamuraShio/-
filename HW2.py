"""Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована."""

string = '000000000000000'
n = 5
for i in range(1, n+1):
    print('string #{}: {}'.format(i, string))


"""Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5."""

n = 10
count = 0
for i in range(n):
    if int(input('введите цифру: ')) == 5:
        count += 1
        print('count is', count)
print('пользователь ввёл значение 5', count, 'раз')


"""Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран."""

n = 100
summ = 0
for i in range(1, n+1):
    summ += i

print('сумма всех чисел от 1 до', n, 'равна:', summ)


"""Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран."""

n = 10
total = 0
for i in range(1, n+1):
    if total == 0:
        total = i
    else:
        total *= i

print('произведение всех чисел от 1 до', n, 'равно:', total)


"""Задача 5
Вывести цифры числа на каждой строчке."""  # sample was given


number = 3819

while number > 0:
    print(number % 10)
    number = number//10


"""Задача 6
Найти сумму цифр числа."""

temp_number = number = 284719
digit_summ = 0
while temp_number > 0:
    digit_summ += (temp_number % 10)
    temp_number = temp_number//10
print('сумма цифр числа', number, 'равна: ', digit_summ)


"""Задача 7
Найти произведение цифр числа."""
temp_number = number = 2847
result = 0
while temp_number > 0:
    if result == 0:
        result = temp_number % 10
    else:
        result *= (temp_number % 10)
    temp_number = temp_number//10
print('произведение цифр числа', number, 'равно: ', result)


"""Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?"""  # sample was given

value = 2134135
while value > 0:
    if value % 10 == 5:
        print('Yes')
        break
    value = value//10
else:
    print('No')


"""Задача 9
Найти максимальную цифру в числе"""

temp_value = value = 823094571
max_value = value % 10
while temp_value > 0:
    if max_value < temp_value % 10:
        max_value = temp_value % 10
    temp_value = temp_value//10
print('максимальная цифра в числе {} равна {}'.format(value, max_value))


"""Задача 10
Найти количество цифр 5 в числе"""

temp_value = value = 152535455
count = 0
while temp_value > 0:
    if temp_value % 10 == 5:
        count += 1
    temp_value = temp_value // 10
print('в числовом ряде', value, 'число 5 встретилось', count, 'раз')
