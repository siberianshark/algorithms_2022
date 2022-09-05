"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

from memory_profiler import profile

@profile
def decor(func):                                                    # 0
    def wrapper(*argv):                                             # 0
        return func(*argv)                                          # 0
    return wrapper                                                  # 0

@ decor
def get_rev_number(number, rev_number = ''):                        # 0
    if number == 0:                                                 # 0
        return rev_number                                           # 0
    else:
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        return get_rev_number(number // 10, rev_number)             # 0.2

@profile
def get_rev_number_2(number, rev_number = ''):                      # 0
    while number != 0:                                              # 0
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        number = number // 10                                       # 0
    return rev_number                                               # 0

number_s = 1230
print(get_rev_number(number_s))
print(get_rev_number_2(number_s))
# print(
#     timeit(
#         "get_rev_number(number_s)",
#         setup="from __main__ import get_rev_number, number_s", number=1000000))
# print(
#     timeit(
#         "get_rev_number_2(number_s)",
#         setup="from __main__ import get_rev_number_2, number_s", number=1000000))


#1 000 000 повторений:
#get_rev_number = 1.291
#get_rev_number_2 = 1.012

#Замена Рекурсии на Цикл привела к снижению сложности и увеличению скорости
#обработки операций с факториальной O(n!) на линейную O(n).
#@profile - показывает, что цикл не нагружает доп. элементы в Increment - что говорит о том,
#что дополнительной опертивной памяти для хранения Итерации не требуется.