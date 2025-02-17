"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""



# сложность O(n)
def get_min_number(lst):
    min_number = lst[0]                                     # O(1)
    for i in lst:                                           # O(n)
        if i < min_number:                                  # O(len(i)
            min_number = i                                  # O(1)
    return min_number                                       # O(1)


# Сложность O(n**2)
def get_min_number_2(lst):
    min_number_2 = lst[0]                                   # O(1)
    for i in lst:                                           # O(n)
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  # O(n)
            if min_number_2 > lst[j]:                       # O(len(lst[j])
                min_number_2 = lst[j]                       # O(1)
    return min_number_2                                     # O(1)


first_list = [100, 50, 3, 4, 23, 10]

print(get_min_number(first_list))

print(get_min_number_2(first_list))