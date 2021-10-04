def main():
    n = int(input('Введите количество шаров: '))
    if n in [1, 2, 4, 7]:
        print('Разложить нельзя')
    x3 = n - n % 3
    x5 = n - x3
    while x3 % 3 != 0 or x5 % 5 != 0:
        x3 -= 3
        x5 += 3

    print(f'Раскладывается как {x3//3}*3 + {x5//5}*5')


if __name__ == '__main__':
    main()
