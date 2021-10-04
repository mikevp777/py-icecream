class CantSolve(Exception):
    """Can't solve ax+by=k in integers"""


def solve_integer(a, b, k):
    if k % b == 0:
        return 0, k // b
    x_a = k - k % a
    y_b = k - x_a
    while y_b % b != 0:
        x_a -= a
        y_b += a
        if x_a < a:
            raise CantSolve
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
        print(f'Раскладывается как {x}*{a} + {y}*{b} = {k}')


if __name__ == '__main__':
    main()
