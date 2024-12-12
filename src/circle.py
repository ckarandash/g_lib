import math

def area(r):
    """Возвращает площадь круга"""
    # Параметры:
    #   r (int): радиус круга
    # Возвращаемое значение:
    #   math.pi * r * r: искомая площадь круга


    if type(r) is not int:
        raise TypeError("Argument должен быть int")

    if r <= 0:
        raise ValueError("Argument должны быть больше нуля")

    return math.pi * r * r

def perimeter(r):
    """Возвращает периметр круга"""
    # Параметры:
    #   r (int): радиус круга
    # Возвращаемое значение:
    #   2 * math.pi * r: искомый периметр круга

    if type(r) is not int:
        raise TypeError("Argument должен быть int")

    if r <= 0:
        raise ValueError("Argument должны быть больше нуля")

    return 2 * math.pi * r

