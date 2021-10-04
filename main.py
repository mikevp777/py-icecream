def main():
    print('Решение уравнения ax+by=k в целых x и у')
    k = int(input('k: '))
    a = int(input('a: '))
    b = int(input('b: '))
    x_a = k - k % a
    x_b = k - x_a
    while x_b % b != 0:
        x_a -= a
        x_b += a
        if x_a < a:
            print('Разложить нельзя')
            return

    print(f'Раскладывается как {x_a//a}*{a} + {x_b//b}*{b} = {k}')


if __name__ == '__main__':
    main()
