# Задание 4
# Напишите Программу - которая работает по принципу алгоритма Шифр Цезаря.
# Нужно создать класс состоящий из 2 методов:
# 1. Метод который ШИФРУЕТ данные.
# 2. Метода который ДЕШИФРУЕТ эти же данные.
# Представим что ваш метод получает слово состоящее из ЛЮБЫХ символов.
# Ваш 1-й метод должен вернуть зашифрованную строку.
# Алгоритм Шифрования: ASCII позиция + 7.
# Алгоритм Дешифровки: Обратная операция Алгоритма Шифрования.

# a = ' abcdefghijklmnopqrstuvwxyz'
# print('введите шаг шифрования')
# n = int(input())
# s = input().strip()
# res = ''
# for c in s:
#     res += a[(a.index(c) + n) % len(a)]
# print('Result: "' + res + '"')

a = 'UvVwWxXyYzZHiIjJkKlLmMnNoaAbBcCdDeEfFgGhOpPqQrRsStTu'
print('введите шаг шифрования')
n = int(input())
print('Введите слово для шифрования')
s = input().strip()
res = ''
for c in s:
    res += a[(a.index(c) + n) % len(a)]
print('Result: "' + res + '"')

a = 'UvVwWxXyYzZHiIjJkKlLmMnNoaAbBcCdDeEfFgGhOpPqQrRsStTu'
print('введите шаг расшифровки')
n = int(input())
print('Введите слово для расшифравки')
s = input().strip()
res = ''
for c in s:
    res += a[(a.index(c) - n) % len(a)]
print('Result: "' + res + '"')