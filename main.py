def main():
    n = int(input('Введите количество шаров: '))
    factor1 = int(input('На сколько раскладывать 1: '))
    factor2 = int(input('На сколько раскладывать 2: '))
    if factor2 < factor1:
        factor1, factor2 = factor2, factor1
    x_factor1 = n - n % factor1
    x_factor2 = n - x_factor1
    while x_factor1 % factor1 != 0 or x_factor2 % factor2 != 0:
        x_factor1 -= factor1
        x_factor2 += factor1
        if x_factor1 < factor1:
            print('Разложить нельзя')
            return

    print(f'Раскладывается как {x_factor1//factor1}*{factor1} + {x_factor2//factor2}*{factor2}')


if __name__ == '__main__':
    main()
