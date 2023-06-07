from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Печатает сообщение с результатом."""
    if your_number <= 0:
        return
    result: float = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {result}')


print(message)
calc(25.5)
