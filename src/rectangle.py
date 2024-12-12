def area(a, b):
    """Возвращает площадь прямоугольника"""
    # Параметры:
    #   a (int): длина прямоугольника
    #   b (int): ширина прямоугольника
    # Возвращаемое значение:
    #   a * b: искомая площадь прямоугольника

    if type(a) is not int or type(b) is not int:
        raise TypeError("Аргументы должны быть int")

    if a <= 0 or b <= 0:
        raise ValueError("Аргументы должны быть больше нуля")

    return a * b

def perimeter(a, b):
    """Возвращает периметр прямоугольника"""

    # Параметры:
    #   a (int): длина прямоугольника
    #   b (int): ширина прямоугольника
    # Возвращаемое значение:
    #   2 * (a + b): искомый периметр прямоугольника

    if type(a) is not int or type(b) is not int:
        raise TypeError("Аргументы должны быть int")

    if a <= 0 or b <= 0:
        raise ValueError("Аргументы должны быть больше нуля")

    return 2 * (a + b)
