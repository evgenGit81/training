# -*- coding: utf-8 -*-
# Игра версии 0.0.1
# Разработчик - Нартов Евгений Александрович
# e-mail: evgeniynrtv@gmail.com
# В игре нет проверки ввода пользователя
import random

def area_print():
    """Печать игрового поля."""
    for i in game_area:
        print(*i)
    print()
def position_area():
    """Печать примера с пронумерованными позициями."""
    for i in example_area:
        print(*i)
    print()
def check_steps():
    for kn in range(3):
        for jk in range(3):
            if game_area[kn][jk] == '*':
                return True

def game_check():
    """Проверка на выигрышь"""
    if game_area[0][1] == 'X' and game_area[1][1] == 'X' and game_area[2][1] == 'X':
        print("Выиграли X")
        return "X"
    elif game_area[0][0] == 'X' and game_area[0][1] == 'X' and game_area[0][2] == 'X':
        print("Выиграли X")
        return "X"
    elif game_area[0][0] == 'X' and game_area[1][0] == 'X' and game_area[2][0] == 'X':
        print("Выиграли X")
        return "X"
    elif game_area[2][0] == 'X' and game_area[1][1] == 'X' and game_area[0][2] == 'X':
        print("Выиграли X")
        return "X"
    elif game_area[2][0] == 'X' and game_area[2][1] == 'X' and game_area[2][2] == 'X':
        print("Выиграли X")
        return "X"
    elif game_area[0][2] == 'X' and game_area[1][2] == 'X' and game_area[2][2] == 'X':
        print("Выиграли X")
        return "X"
    elif game_area[0][1] == '0' and game_area[1][1] == '0' and game_area[2][1] == '0':
        print("Выиграли 0")
        return "0"
    elif game_area[0][0] == '0' and game_area[0][1] == '0' and game_area[0][2] == '0':
        print("Выиграли 0")
        return "0"
    elif game_area[0][0] == '0' and game_area[1][0] == '0' and game_area[2][0] == '0':
        print("Выиграли 0")
        return "0"
    elif game_area[2][0] == '0' and game_area[1][1] == '0' and game_area[0][2] == '0':
        print("Выиграли 0")
        return "0"
    elif game_area[2][0] == '0' and game_area[2][1] == '0' and game_area[2][2] == '0':
        print("Выиграли 0")
        return "0"
    elif game_area[0][2] == '0' and game_area[1][2] == '0' and game_area[2][2] == '0':
        print("Выиграли 0")
        return "0"
    else:
        if check_steps() == True:
            print("Есть еще ход")
            return "M"
        else:
            print("Ничья")
            return "N"

def writ_x():
    """Замещает звездочки крестиками (для AI)"""
    for k in range(3):
        mk = 0
        for i in range(3):
            if game_area[i][k] == '*':
                game_area[i][k] = 'X'
                mk = 1
                break
        if mk == 1:
            break
    return game_area

def writ_0():
    """Замещает звездочки нолями (для AI)"""
    for k in range(3):
        mn = 0
        for i in range(3):
            if game_area[i][k] == '*':
                game_area[i][k] = '0'
                mn = 1
                break
        if mn == 1:
            break
    return game_area

def call_check():
    """Вызывает проверку от 3х ходов"""
    if count >= 3:
        if game_check() == 'X' or game_check() == '0' or game_check() == 'N':
            return True

def ai_go_first(count):
    """Функция первого хода AI"""
    user_enter = input('Ваш выбор: ')
    if user_enter == '1':
        game_area[0][0] = '0'
        if count == 1:
            if game_area[1][0] == '*' and game_area[0][1] == '*':
                game_area[0][1] = 'X'
        if count == 2:
            if game_area[0][1] == '0' and game_area[2][1] == '*':
                game_area[2][1] = 'X'
            elif game_area[1][0] == '0' and game_area[0][1] == '0':
                game_area[0][2] = 'X'
            elif game_area[1][0] == '*' and game_area[0][1] == '*':
                game_area[0][1] = 'X'
        if count >= 3:
            writ_x()

    elif user_enter == '2':
        game_area[0][1] = '0'
        if count == 1:
            if game_area[0][0] == '*' and game_area[0][2] == '*':
                game_area[0][0] = 'X'
        if count == 2:
            if game_area[0][0] == '0' and game_area[0][2] == '*':
                game_area[0][2] = 'X'
            elif game_area[0][0] == '*' and game_area[0][2] == '0':
                game_area[0][0] = 'X'
            elif game_area[0][0] == '*' and game_area[0][2] == '*':
                game_area[0][0] = 'X'
        if count >= 3:
            writ_x()

    elif user_enter == '3':
        game_area[0][2] = '0'
        if count == 1:
            if game_area[0][1] == '*' and game_area[1][2] == '*':
                game_area[0][1] = 'X'
        if count == 2:
            if game_area[0][1] == '0' and game_area[0][0] == '*':
                game_area[0][0] = 'X'
            elif game_area[1][2] == '0' and game_area[2][2] == '*':
                game_area[2][2] = 'X'
            elif game_area[0][1] == '*' and game_area[1][2] == '*':
                game_area[0][1] = 'X'
        if count >= 3:
            writ_x()

    elif user_enter == '4':
        game_area[1][0] = '0'
        if count == 1:
            if game_area[0][0] == '*' and game_area[2][0] == '*':
                game_area[0][0] = 'X'
        if count == 2:
            if game_area[0][0] == '0' and game_area[2][0] == '*':
                game_area[2][0] = 'X'
            elif game_area[2][0] == '0' and game_area[0][0] == '*':
                game_area[0][0] = 'X'
            elif game_area[0][0] == '*' and game_area[2][0] == '*':
                game_area[0][0] = 'X'
        if count >= 3:
            writ_x()

    elif user_enter == '6':
        game_area[1][2] = '0'
        if count == 1:
            if game_area[2][2] == '*' and game_area[0][2] == '*':
                game_area[2][2] = 'X'
        if count == 2:
            if game_area[2][2] == '0' and game_area[0][2] == '*':
                game_area[0][2] = 'X'
            elif game_area[2][2] == '*' and game_area[0][2] == '0':
                game_area[2][2] = 'X'
            elif game_area[2][2] == '*' and game_area[0][2] == '*':
                game_area[2][2] = 'X'
        if count >= 3:
            writ_x()

    elif user_enter == '7':
        game_area[2][0] = '0'
        if count == 1:
            if game_area[1][0] == '*' and game_area[2][1] == '*':
                game_area[1][2] = 'X'
        if count == 2:
            if game_area[1][0] == '0' and game_area[0][0] == '*':
                game_area[0][0] = 'X'
            elif game_area[2][2] == '*' and game_area[2][1] == '0':
                game_area[2][2] = 'X'
            elif game_area[1][0] == '*' and game_area[2][1] == '*':
                game_area[1][2] = 'X'
        if count >= 3:
            writ_x()

    elif user_enter == '8':
        game_area[2][1] = '0'
        if count == 1:
            if game_area[2][0] == '*' and game_area[2][2] == '*':
                game_area[2][0] = 'X'
        if count == 2:
            if game_area[2][0] == '0' and game_area[2][2] == '*':
                game_area[2][2] = 'X'
            elif game_area[2][0] == '*' and game_area[2][2] == '0':
                game_area[2][0] = 'X'
            elif game_area[2][0] == '*' and game_area[2][2] == '*':
                game_area[2][0] = 'X'

        if count >= 3:
            writ_x()

    elif user_enter == '9':
        game_area[2][2] = '0'
        if count == 1:
            if game_area[1][2] == '*' and game_area[2][1] == '*':
                game_area[2][1] = 'X'
        if count == 2:
            if game_area[1][2] == '0' and game_area[2][1] == '*':
                game_area[2][1] = 'X'
            elif game_area[1][2] == '*' and game_area[2][1] == '0':
                game_area[1][2] = 'X'
            elif game_area[1][2] == '*' and game_area[2][1] == '*':
                game_area[2][1] = 'X'
        if count >= 3:
            writ_x()

def user_go_first(count):
    user_enter = input('Ваш выбор: ')
    if user_enter == '1':
        game_area[0][0] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            elif game_area[1][0] == '*' and game_area[0][1] == '*':
                game_area[0][1] = '0'
        if count == 2:
            if game_area[0][1] == 'X' and game_area[2][1] == '*':
                game_area[2][1] = '0'
            elif game_area[1][0] == 'X' and game_area[0][1] == 'x':
                game_area[0][2] = '0'
            elif game_area[1][0] == '*' and game_area[0][1] == '*':
                game_area[0][1] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '2':
        game_area[0][1] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            elif game_area[0][0] == '*' and game_area[0][2] == '*':
                game_area[0][0] = '0'
        if count == 2:
            if game_area[0][0] == 'X' and game_area[0][2] == '*':
                game_area[0][2] = '0'
            elif game_area[0][0] == '*' and game_area[0][2] == 'X':
                game_area[0][0] = '0'
            elif game_area[0][0] == '*' and game_area[0][2] == '*':
                game_area[0][0] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '3':
        game_area[0][2] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            elif game_area[0][1] == '*' and game_area[1][2] == '*':
                game_area[0][1] = '0'
        if count == 2:
            if game_area[0][1] == 'X' and game_area[0][0] == '*':
                game_area[0][0] = '0'
            elif game_area[1][2] == 'X' and game_area[2][2] == '*':
                game_area[2][2] = '0'
            elif game_area[0][1] == '*' and game_area[1][2] == '*':
                game_area[0][1] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '4':
        game_area[1][0] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            if game_area[0][0] == '*' and game_area[2][0] == '*':
                game_area[0][0] = '0'
        if count == 2:
            if game_area[0][0] == 'X' and game_area[2][0] == '*':
                game_area[2][0] = '0'
            if game_area[2][0] == 'X' and game_area[0][0] == '*':
                game_area[0][0] = '0'
            if game_area[0][0] == '*' and game_area[2][0] == '*':
                game_area[0][0] = '0'
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '6':
        game_area[1][2] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            elif game_area[2][2] == '*' and game_area[0][2] == '*':
                game_area[2][2] = '0'
        if count == 2:
            if game_area[2][2] == 'X' and game_area[0][2] == '*':
                game_area[0][2] = '0'
            elif game_area[2][2] == '*' and game_area[0][2] == 'X':
                game_area[2][2] = '0'
            elif game_area[2][2] == '*' and game_area[0][2] == '*':
                game_area[2][2] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '7':
        game_area[2][0] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            elif game_area[1][0] == '*' and game_area[2][1] == '*':
                game_area[1][2] = '0'
        if count == 2:
            if game_area[1][0] == 'X' and game_area[0][0] == '*':
                game_area[0][0] = '0'
            elif game_area[2][2] == '*' and game_area[2][1] == 'X':
                game_area[2][2] = '0'
            elif game_area[1][0] == '*' and game_area[2][1] == '*':
                game_area[1][2] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '8':
        game_area[2][1] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            elif game_area[2][0] == '*' and game_area[2][2] == '*':
                game_area[2][0] = '0'
        if count == 2:
            if game_area[2][0] == 'X' and game_area[2][2] == '*':
                game_area[2][2] = '0'
            elif game_area[2][0] == '*' and game_area[2][2] == 'X':
                game_area[2][0] = '0'
            elif game_area[2][0] == '*' and game_area[2][2] == '*':
                game_area[2][0] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'
        if count >= 3:
            writ_0()

    elif user_enter == '9':
        game_area[2][2] = 'X'
        if count == 1:
            if game_area[1][1] == '*':
                game_area[1][1] = '0'
            if game_area[1][2] == '*' and game_area[2][1] == '*':
                game_area[2][1] = '0'
        if count == 2:
            if game_area[1][2] == 'X' and game_area[2][1] == '*':
                game_area[2][1] = '0'
            elif game_area[1][2] == '*' and game_area[2][1] == 'X':
                game_area[1][2] = '0'
            elif game_area[1][1] == '*':
                game_area[1][1] = '0'

        if count >= 3:
            writ_0()
            
    elif user_enter == 5:
        game_area[1][1] = "X"

def user_request():

    global position_u1
    global position_u2
    position_u1 = int(input("Куда поставит первый игрок нолик? "))
    print()
    position_u2 = int(input("Куда поставит второй игрок крестик? "))
    print("posit1 = ", position_u1, "posit2 = ", position_u2)



def users_steps():
    user_request()
    pos1 = position_u1
    pos2 = position_u2
    print("pos1 = ", pos1, "pos2 = ", pos2)
    if position_u1 == 1 and game_area[0][0] == '*':
        game_area[0][0] = "0"
    if position_u1 == 2 and game_area[0][1] == "*":
        game_area[0][1] = "0"
    if position_u1 == 3 and game_area[0][2] == "*":
        game_area[0][2] = "0"
    if position_u1 == 4 and game_area[1][0] == "*":
        game_area[1][0] = "0"
    if position_u1 == 5 and game_area[1][1] == "*":
        game_area[1][1] = "0"
    if position_u1 == 6 and game_area[1][2] == "*":
        game_area[1][2] = "0"
    if position_u1 == 7 and game_area[2][0] == "*":
        game_area[2][0] = "0"
    if position_u1 == 8 and game_area[2][1] == "*":
        game_area[2][1] = "0"
    if position_u1 == 9 and game_area[2][2] == "*":
        game_area[2][2] = "0"


    if position_u2 == 1 and game_area[0][0] == '*':
        game_area[0][0] = "X"
    if position_u2 == 2 and game_area[0][1] == "*":
        game_area[0][1] = "X"
    if position_u2 == 3 and game_area[0][2] == "*":
        game_area[0][2] = "X"
    if position_u2 == 4 and game_area[1][0] == "*":
        game_area[1][0] = "X"
    if position_u2 == 5 and game_area[1][1] == "*":
        game_area[1][1] = "X"
    if position_u2 == 6 and game_area[1][2] == "*":
        game_area[1][2] = "X"
    if position_u2 == 7 and game_area[2][0] == "*":
        game_area[2][0] = "X"
    if position_u2 == 8 and game_area[2][1] == "*":
        game_area[2][1] = "X"
    if position_u2 == 9 and game_area[2][2] == "*":
        game_area[2][2] = "X"

    #else:
    #    print("Позиция занята, повторите ввод.")
     #   user_request()


    return game_area

game_area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
example_area = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


while True:
    us_ch = input('Если хотитет играть с другим игроком, то введите "Y" ')
    if us_ch == "Y" or us_ch == "y":
        print("Вы выбрали играть с человеком. Приятной игры.")
        print("Первыми ходят нолики")
        print("Вводите номер позиции куда хотите поставить нолик или крестик (расположение позиций смотрите ниже).")
        position_area()
        print("Ниже ваше игровое поле.")
        area_print()
        #position_u1 = 0
        #position_u2 = 0
        count = 0
        for ik in range(10):
            count += 1
            users_steps()
            area_print()
            if call_check() == True:
                break

    else:
        print("Вы выбрали игру с AI. Начинаем!")
        m = random.randint(1, 3)

        n = int(input("""Прежде, чем начнем играть, определимся кто начнет первым.
        Загадай число от 1 до 3. Если ты угадаешь мое, то начинаешь ты, 
        в противном случае, начинаю я. """))

        print("_______________________")
        if m == n:
            chose = "user"
            print(f'Ты начинаешь. Мойе число {m}')
            print("Твои крестики Х, мои - 0")
        else:
            chose = "AI"
            print(f'Я начинаю. Мое число {m}')
            print("Твои нолики 0, мои - X")

        print("_______________________")
        print("Наше игровое поле.")
        area_print()

        chose_strat = random.randint(1, 2)

        if chose_strat == 1:
            """Был произведен выбор компьютером жестко прописанной стратегии игры"""
            if chose == "AI":
                game_area[1][1] = 'X'
                print("____________")
                print("Я сделал свой ход.")
                area_print()
                count = 0
                for ki in range(5):
                    count += 1
                    print("""Куда поставите свой "0" - в верхний угол справа, введите 3,
                    если в верхний левый угол, введите 1, если в середину вверху
                    введите 2, если в середину крайнего левого столбца, введите 4,
                    если в середину крайнего правого столбца, введите 6, если 
                    в нижний левый угол, введите 7, если в середину нижней строки,
                    введите 8, если в левый нижний угол, введите 9?""")
                    ai_go_first(count)
                    print(count)
                    area_print()
                    # call_check()
                    if call_check() == True:
                        break

            if chose == "user":
                print("____________")
                print("Начинай свой ход.")
                print()
                print("""Куда поставите свой "X" - в верхний угол справа, введите 3,
                    если в верхний левый угол, введите 1, если в середину вверху
                    введите 2, если в середину крайнего левого столбца, введите 4,
                    если в середину крайнего правого столбца, введите 6, если 
                    в нижний левый угол, введите 7, если в середину нижней строки,
                    введите 8, если в левый нижний угол, введите 9?""")
                count = 0
                area_print()
                for ki in range(5):
                    count += 1
                    user_go_first(count)
                    print(count)
                    area_print()
                    if call_check() == True:
                        break

        elif chose_strat == 1:
            """В этой стратегии компьютер в первой свободной ячейке ставит либо крестик либо нолик"""
            if chose == "AI":
                game_area[1][1] = 'X'
                print("____________")
                print("Я сделал свой ход.")
                area_print()
                count = 0
                for ki in range(5):
                    count += 1
                    print("""Куда поставите свой "0" - в верхний угол справа, введите 3,
                                   если в верхний левый угол, введите 1, если в середину вверху
                                   введите 2, если в середину крайнего левого столбца, введите 4,
                                   если в середину крайнего правого столбца, введите 6, если 
                                   в нижний левый угол, введите 7, если в середину нижней строки,
                                   введите 8, если в левый нижний угол, введите 9?""")
                    print()
                    user_enter = input('Ваш выбор: ')
                    if user_enter == '1':
                        game_area[0][0] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == '2':
                        game_area[0][1] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "3":
                        game_area[0][1] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "4":
                        game_area[1][0] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "6":
                        game_area[1][2] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "7":
                        game_area[2][0] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "8":
                        game_area[2][1] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "9":
                        game_area[2][2] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
            if chose == "user":
                print("____________")
                print("Начинай свой ход.")
                print()
                print("""Куда поставите свой "X" - в верхний угол справа, введите 3,
                    если в верхний левый угол, введите 1, если в середину вверху
                    введите 2, если в середину крайнего левого столбца, введите 4,
                    если в середину крайнего правого столбца, введите 6, если 
                    в нижний левый угол, введите 7, если в середину нижней строки,
                    введите 8, если в левый нижний угол, введите 9?""")
                count = 0
                area_print()
                for ki in range(5):
                    count += 1
                    print("""Куда поставите свой "0" - в верхний угол справа, введите 3,
                                                       если в верхний левый угол, введите 1, если в середину вверху
                                                       введите 2, если в середину крайнего левого столбца, введите 4,
                                                       если в середину крайнего правого столбца, введите 6, если 
                                                       в нижний левый угол, введите 7, если в середину нижней строки,
                                                       введите 8, если в левый нижний угол, введите 9?""")
                    print()
                    user_enter = input('Ваш выбор: ')
                    if user_enter == '1':
                        game_area[0][0] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == '2':
                        game_area[0][1] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "3":
                        game_area[0][1] = "0"
                        writ_x()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "4":
                        game_area[1][0] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "6":
                        game_area[1][2] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "7":
                        game_area[2][0] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "8":
                        game_area[2][1] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break
                    if user_enter == "9":
                        game_area[2][2] = "X"
                        writ_0()
                        area_print()
                        if call_check() == True:
                            break

        next_chose = input('Если хотите продолжить играть, введите "Y"?')
        if next_chose != "Y" or next_chose != "y":
            break
    next_chose = input('Если хотите продолжить играть, введите "Y"?')
    if next_chose != "Y" or next_chose != "y":
        break





