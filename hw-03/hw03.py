# Перевірка паролю
# password = 'password123'

# input = 'password'
# if input == password:
#     print('Ви увійшли в систему')
# else:
#     print('Пароль невірний')

# Визначення днів тижня
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# day = 6
# if 0 <= day < 7:
#     print(days[day])
# else:
#     print('Invalid day number')

# Таблиця множення
# num = 5
# for i in range(1, 11):
#     print(f'{num} x {i} = {num * i}')

# Сума чисел
# numbers = [3, 5, 9, 1, 2, 8, 7, 6, 4]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)

# Факторіал числа
# n = 5

# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1

# print('Factorial: ', factorial)

# Парні числа
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# Пошук простих чисел
import math

num1=2
num2=15

print('Пошук простих чисел: ')
if num1 == 2:
    print(num1)

for i in range ((num1 // 2) * 2 + 1, num2 + 1, 2):
    is_prime = True
    for j in range (3, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)