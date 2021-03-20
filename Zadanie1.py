# Задание 1
# При заданном целом числе n посчитайте n + nn + nnn.
# Выполнить задачу с помощью класса.



# n = int(input("Введите число n: "))
# temp = str(n)
# t1 = temp + temp
# t2 = temp + temp + temp
# comp = n + int(t1) + int(t2)
# print("Результат равен:", comp)


# a = int(input(" Введите число n: "))
# p = 0
# for i in range(1, a+1):
#  p += int(str(a)*i)
# print(p)


# a = int(input(" Введите число n: "))
# p = 0
# for i in range(1, a+1):
#  p += int(str(a)*i)
# print(p)

# Leo Ruitter, [20.03.21 18:59]
class task1:
    def __init__(self):
        n = int(input("Введите число n: "))
        temp = str(n)
        t1 = temp + temp
        t2 = temp + temp + temp
        comp = n + int(t1) + int(t2)
        print("Результат равен:", comp)

t1= task1()