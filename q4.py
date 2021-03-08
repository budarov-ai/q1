n = int(input('Загадай число, пожалуйста. :'))

#попытка реализовать проверку не получилась проверка на дроби
rules1 = n <= 0
#rules2 = n = float

if rules1:
    print('Загадай целое положительное число, пожалуйста.')
    n = int(input('Загадай число :'))
max_n = 0
while n > 0:
    m = n % 10
    if  m >= max_n:
        max_n = m
        n //= 10
print(max_n)

