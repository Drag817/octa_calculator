def add(a, b):
    sum = ''
    length = max(len(a), len(b))
    next_num = 0

    a = f'{a[::-1]}' + '0' * (length - len(a))
    b = f'{b[::-1]}' + '0' * (length - len(b))

    for i in range(length):
        digit = (int(a[i]) + int(b[i]) + next_num) % 8
        next_num = (int(a[i]) + int(b[i]) + next_num) // 8
        sum += f'{digit}'

    if next_num > 0:
        sum += f'{next_num}'

    return sum[::-1]


def subt(a, b):
    subtact = ''
    mines = ''
    length = max(len(a), len(b))
    next_num = 0

    if int(b) > int(a):
        b, a = f'{a[::-1]}' + '0' * (length - len(a)), f'{b[::-1]}' + '0' * (length - len(b))
        mines = '-'
    else:
        a = f'{a[::-1]}' + '0' * (length - len(a))
        b = f'{b[::-1]}' + '0' * (length - len(b))

    for k in range(length):
        if (int(a[k]) - int(b[k]) - next_num) < 0:
            digit = (int(a[k]) + 8 - int(b[k]) - next_num) % 8
            next_num = 1
        else:
            digit = (int(a[k]) - int(b[k]) - next_num) % 8
            next_num = 0

        subtact += f'{digit}'
    subtact += mines

    return subtact[::-1]


def mult(a, b):
    res = []
    a = f'{a[::-1]}'
    b = f'{b[::-1]}'

    for i in range(len(b)):
        buf = ''
        next_num = 0

        for j in range(len(a)):
            digit = (int(a[j]) * int(b[i]) + next_num) % 8
            next_num = (int(a[j]) * int(b[i]) + next_num) // 8
            buf += f'{digit}'

        if next_num > 0:
            buf += f'{next_num}'

        if len(b) > 1:
            res.append(f'{buf[::-1]}' + '0' * i)
        else:
            return buf[::-1]

    for i in range(len(res) - 1):
        res[i + 1] = add(res[i], res[i + 1])

    return res[-1]


def main():
    print()
    print('1) Сложение\n'
          '2) Вычитание\n'
          '3) Умножение')

    choise = input('Выберите функцию: ')

    if choise not in ['1', '2', '3']:
        print('Неверный ввод, повторите попытку!')
        main()

    a = input('Введите первое число: ')
    b = input('Введите второе число: ')

    if choise == '1':
        print(f'Сумма чисел = {add(a, b)}')
    elif choise == '2':
        print(f'Разность чисел = {subt(a, b)}')
    elif choise == '3':
        print(f'Произведение чисел = {mult(a, b)}')

    cont = input('Продолжить y/n? ')

    if cont == 'y':
        main()
    else:
        quit()


if __name__ == '__main__':
    main()
