from random import randint
import math


def test_greeting():
    # """
    # Напишите программу, которая выводит на экран приветствие.
    # """
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


#
def test_rectangle():
    #     """
    #     Напишите программу, которая берет длину и ширину прямоугольника
    #     и считает его периметр и площадь.
    #     """
    a = 10
    b = 20
    perimeter = 2 * (a + b)
    #     # TODO сосчитайте периметр
    assert perimeter == 60
    #     # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = math.pi * r ** 2
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * math.pi * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    list = [randint(1, 100) for i in range(10)]
    l = sorted(list)
    print(l)
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    # TODO удалите повторяющиеся элементы
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    list_clear = [l[0]]
    i = 1
    index_list = 0

    while i < len(l):
        if list_clear[index_list] != l[i]:
            list_clear.append(l[i])
            index_list += 1
        i += 1
    l = list_clear

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    # TODO создайте словарь
    d = (dict(zip(first, second)))
    print(d.values())

    assert isinstance(d, dict)
    assert len(d) == 5
