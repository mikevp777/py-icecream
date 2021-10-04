class CantSolve(Exception):
    pass


def solve_integer(a, b, k):

    # Проверка условия: "k делится на b нацело"
    # без этой проверки в некоторых случаях алгоритм не сработает
    # Если делится - решение найдено

    result = []

    if k % b == 0:
        result += (0, k // b)

    # Сам алгоритм (проверка что k делится на a нацело в нем уже заложена):

    x_a = k - k % a
    y_b = k - x_a
    while x_a >= a:
        if y_b % b == 0:
            result.append([x_a//a, y_b//b])
        x_a -= a
        y_b += a
    if result:
        return result
    raise CantSolve  # если решения нет - вызывает исключение


def main():
    print('Решение уравнения ax+by=k в целых x и у')
    k = int(input('k: '))
    a = int(input('a: '))
    b = int(input('b: '))
    try:
        solutions = solve_integer(a, b, k)
    except CantSolve:
        print('Не раскладывается')
    else:
        for x, y in solutions:
            print(f'Раскладывается как {x}*{a} + {y}*{b} = {x*a+y*b}')


if __name__ == '__main__':
    main()
