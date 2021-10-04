class CantSolve(Exception):
    pass


def solve_integer(a, b, k):

    # Проверка условия: "k делится на b нацело"
    # без этой проверки в некоторых случаях алгоритм не сработает
    # Если делится - решение найдено

    if k % b == 0:
        return 0, k // b

    # Сам алгоритм (проверка что k делится на a нацело в нем уже заложена):

    x_a = k - k % a
    y_b = k - x_a
    while y_b % b != 0:
        x_a -= a
        y_b += a
        if x_a < a:
            raise CantSolve  # если решения нет - вызывает исключение
    return x_a//a, y_b//b


def main():
    print('Решение уравнения ax+by=k в целых x и у')
    k = int(input('k: '))
    a = int(input('a: '))
    b = int(input('b: '))
    try:
        x, y = solve_integer(a, b, k)
    except CantSolve:
        print('Не раскладывается')
    else:
        print(f'Раскладывается как {x}*{a} + {y}*{b} = {x*a+y*b}')


if __name__ == '__main__':
    main()
