def game():
    print("Привествую тебя в игре крестики-нолики ")
    print("Будем играть на поле 3х3")
    print("Правила игры: можно ставть 0, 1 или 2")
game()

field = [[" "] * 3 for i in range(3) ]
def show():
    print(("  0 1 2"))
    for i, row in enumerate(field):
        row_str = str(i) + " " + " ".join(map(str, row))
        print(row_str)
show()

def ask():
    while True:
        cords = input("         Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 0 1 или 2 ")
            continue
        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Победу одержал X!")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Победу одержал 0!")
            return True
    return False
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break