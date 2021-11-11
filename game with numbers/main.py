import random


def help_command(action):
    if action == 'ediff':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        ediff('')
    elif action == 'emode':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        emode('')
    elif action == 'add':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        addition()
    elif action == 'sub':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        subtracting()
    elif action == 'mul':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        multiply()
    elif action == 'div':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        divide()
    elif action == 'div(int)':
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')
        divide_with_rounding()
    else:
        print('\n\n\t\t\t\tКомманда "help"\n================================================\n'
              'exit - выход с игры\n\n'
              'Уровени сложности:\n'
              '\te - легкий(-10, 10)\n\tm - средний(-100, 100)\n\th - тяжелый(-1000, 1000)\n'
              'ediff - команда для изменения режима сложности\n\nРежимы игры:\n'
              '\tadd - сложение\n\tsub - вычитание\n\tmul - умножение\n\tdiv - деление\n\tdiv(int) - деление, '
              'но ответ вписывать с округлением\n '
              'emode - команда для изменения режима игры\n\n')


def random_numbers():
    global num1, num2
    num1 = int(random.randint(numberValue, numberValue1))
    num2 = int(random.randint(numberValue, numberValue1))


def addition():
    equal = input(f'{num1} + {num2} = ?\n')
    try:
        int(equal)

        if int(equal) == num1 + num2:
            print('\033[1;32;40m Правильный ответ! \033[0m')
        elif int(equal) != num1 + num2:
            print(f'\033[1;31;40m Правильный ответ: {num1 + num2} \033[0m')
    except ValueError:
        if equal == 'exit':
            exit()
        elif equal == 'ediff':
            ediff('add')
            print('\033[1;36;40m Уровень сложности успешно изменён \033[0m')
            random_numbers()
            addition()
        elif equal == 'help':
            help_command('add')
        elif equal == 'emode':
            emode('add', 'reload')
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        print('\033[1;31;40m ОШИБКА \033[0m')
        addition()
    random_numbers()
    addition()


def subtracting():
    equal = input(f'{num1} - {num2} = ?\n')
    try:
        int(equal)

        if int(equal) == num1 - num2:
            print('\033[1;32;40m Правильный ответ! \033[0m')
        elif int(equal) != num1 - num2:
            print(f'\033[1;31;40m Правильный ответ это: {num1 - num2} \033[0m')
    except ValueError:
        if equal == 'exit':
            exit()
        elif equal == 'ediff':
            ediff('sub')
            print('\033[1;36;40m Уровень сложности успешно изменён \033[0m')
            random_numbers()
            subtracting()
        elif equal == 'help':
            help_command('sub')
        elif equal == 'emode':
            emode('sub', 'reload')
        print('\033[1;31;40m ОШИБКА \033[0m')
        subtracting()
    random_numbers()
    subtracting()


def multiply():
    equal = input(f'{num1} * {num2} = ?\n')
    try:
        int(equal)
        if int(equal) == num1 * num2:
            print('\033[1;32;40m Правильный ответ! \033[0m')
        elif int(equal) != num1 + num2:
            print(f'\033[1;31;40m Правильный ответ это: {num1 * num2} \033[0m')
    except ValueError:
        if equal == 'exit':
            exit()
        elif equal == 'ediff':
            ediff('mul')
            print('\033[1;36;40m Уровень сложности успешно изменён \033[0m')
            random_numbers()
            multiply()
        elif equal == 'help':
            help_command('mul')
        elif equal == 'emode':
            emode('mul', 'reload')
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        print('\033[1;31;40m ОШИБКА \033[0m')
        multiply()
    random_numbers()
    multiply()


def divide_with_rounding():
    if num2 == 0:
        return 0
    equal = input(f'{num1} / {num2} = ?\n')
    try:
        int(equal)
        tempRounding = num1 / num2
        rounding = int(tempRounding + (0.5 if tempRounding > 0 else -0.5))
        if int(equal) == rounding:
            print('\033[1;32;40m Правильный ответ! \033[0m')
        elif int(equal) != rounding:
            print(f'\033[1;31;40m Правильный ответ: {rounding} \033[0m')
    except ValueError:
        if equal == 'exit':
            exit()
        elif equal == 'ediff':
            ediff('div(int)')
            random_numbers()
            divide_with_rounding()
        elif equal == 'help':
            help_command('div(int)')
        elif equal == 'emode':
            emode('div(int)', 'reload')
        print('\033[1;31;40m ОШИБКА \033[0m')
        divide_with_rounding()
    random_numbers()
    divide_with_rounding()


def divide():
    if num2 == 0:
        return 0
    equal = input(f'{num1} / {num2} = ?\n')
    try:
        int(equal)
        if int(equal) == num1 / num2:
            print('\033[1;32;40m Правильный ответ! \033[0m')
        elif int(equal) != num1 / num2:
            print(f'\033[1;31;40m Правильный ответ: {num1 / num2} \033[0m')
    except ValueError:
        if equal == 'exit':
            exit()
        elif equal == 'ediff':
            ediff('div')
            print('\033[1;36;40m Уровень сложности успешно изменён \033[0m')
            random_numbers()
            divide()
        elif equal == 'help':
            help_command('div')
        elif equal == 'emode':
            emode('div', 'reload')
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        print('\033[1;31;40m ОШИБКА \033[0m')
        divide()
    random_numbers()
    divide()


def emode(action, change=''):
    tempChoice = input('Выберите режим игры(add, sub, mul, div, div(int):\n')
    if tempChoice == 'add':
        if change == 'reload':
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        random_numbers()
        addition()
    elif tempChoice == 'sub':
        if change == 'reload':
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        random_numbers()
        subtracting()
    elif tempChoice == 'mul':
        if change == 'reload':
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        random_numbers()
        multiply()
    elif tempChoice == 'div(int)':
        if change == 'reload':
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        random_numbers()
        divide_with_rounding()
    elif tempChoice == 'div':
        if change == 'reload':
            print('\033[1;36;40m Режим игры успешно изменён \033[0m')
        random_numbers()
        divide()
    elif tempChoice == 'exit':
        exit()
    elif tempChoice == 'help':
        help_command('emode')
    else:
        print('\033[1;31;40m ОШИБКА \033[0m')
        if action == 'add':
            addition()
        elif action == 'sub':
            subtracting()
        elif action == 'mul':
            multiply()
        elif action == 'div':
            divide()
        elif action == 'div(int)':
            divide_with_rounding()
        else:
            emode('')


def ediff(action):
    global numberValue, numberValue1
    tempChoice = input('Выберите уровень сложности(e, m, h):\n')
    if tempChoice == 'e':
        numberValue = -10
        numberValue1 = 10
    elif tempChoice == 'm':
        numberValue = -100
        numberValue1 = 100
    elif tempChoice == 'h':
        numberValue = -1000
        numberValue1 = 1000
    elif tempChoice == 'exit':
        exit()
    elif tempChoice == 'help':
        help_command('ediff')
    else:
        if action == 'add':
            print('\033[1;31;40m ОШИБКА \033[0m')
            addition()
        elif action == 'sub':
            print('\033[1;31;40m ОШИБКА \033[0m')
            subtracting()
        elif action == 'mul':
            print('\033[1;31;40m ОШИБКА \033[0m')
            multiply()
        elif action == 'div':
            print('\033[1;31;40m ОШИБКА \033[0m')
            divide()
        elif action == 'div(int)':
            print('\033[1;31;40m ОШИБКА \033[0m')
            divide_with_rounding()
        else:
            print('\033[1;31;40m ОШИБКА \033[0m')
            ediff('')


help_command('')
ediff('')
emode('')

if __name__ == '__main__':
    print('R.I.P.')
