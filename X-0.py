def greet():  # Правила игры
    print("----------------------------")
    print("    Игра крестики-нолики    ")
    print("----------------------------")
    print("     Размер поля  10х10     ")
    print("     формат ввода   x y     ")
    print("  x - строка,  y - столбец  ")
    print("   для  победы - занять 5   ")
    print("клеток  подряд по вертикали,")
    print(" горизонтали или диагонали  ")
    print("----------------------------")


def show():  # Построение поля
    print()
    print("    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ")
    print("  ------------------------------------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ------------------------------------------- ")
    print()


def ask():  # Ввод хода, проверка диапазона ввода и занятость клетки
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 9 or 0 > y or y > 9:
            print(" Координаты вне диапазона! ")
            continue

        if field[y][x] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def calc_line(x, y, x_step, y_step):  # подсчет значений на линии
    val = field[y][x]

    val_count = 0
    for num in range(5):
        if 0 <= x + num * x_step <= 9 and 0 <= y + num * y_step <= 9:
            if field[y + num * y_step][x + num * x_step] == val:
                val_count += 1
            else:
                break
        else:
            break
    for num in range(1, 5):
        if 0 <= x - num * x_step <= 9 and 0 <= y - num * y_step <= 9:
            if field[y - num * y_step][x - num * x_step] == val:
                val_count += 1
            else:
                break
        else:
            break
    return val_count


def check_win(x, y):  # Проверка на победу (всех линий через введенную клетку)
    val_counts = []
    val_count = calc_line(x, y, 0, 1)  # по вертикали
    val_counts.append(val_count)
    val_count = calc_line(x, y, 1, 0)  # по горизонтали
    val_counts.append(val_count)
    val_count = calc_line(x, y, 1, 1)  # по диагонали слева направо вниз
    val_counts.append(val_count)
    val_count = calc_line(x, y, 1, -1)  # по диагонали  слева направо вверх
    val_counts.append(val_count)
    val_count = max(val_counts)

    if val_count >= 5:
        show()
        if field[x][y] == 0:
            print("Победил 0")
        else:
            print("Победил X")
            return True
    return False


while True:
    greet()  # Вызов правил игры
    field = [[" "] * 10 for i in range(10)]  # Очистка игрового поля
    count = 0  # очистка счетчика ходов

    while True:  # игровой процесс
        count += 1
        show()
        if count % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")

        x, y = ask()

        if count % 2 == 1:
            field[y][x] = "X"
        else:
            field[y][x] = "0"

        if check_win(x, y):
            break

        if count == 100:
            print(" Ничья!")
            break

    if input('Хотите сыграть еще? - введите y') != 'y':
        print('До новых встреч!!!')
        break
