from random import randint # для получения случайных координат


class Dot:
# Класс "Точка" содержит координаты "х" и "у"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод сравнения точек по координатам
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Метод вывода в печать точек в формате "(х, у)"
    def __repr__(self):
        return f"({self.x}, {self.y})"

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass

class Ship:
# Класс "Корабли"
    def __init__(self, keel_ship, len_ship, orient_ship):
        self.keel_ship = keel_ship # Киль - нос коробля
        self.len_ship = len_ship # длина коробля
        self.orient_ship = orient_ship # ориентация корабля в пространстве поля, принимает значение 0 - ось Х или 1 - ось У
        self.health = len_ship # здоровье коробля - его длина

    @property
    def dots(self): #метод возвращающий список клеток корабля
        ship_dots = [] #Список точек кораблей
        for i in range(self.len_ship): # цикл выполняется количесвто раз соответствующее длине корабля
            ship_x = self.keel_ship.x # задаю начальные координаты коробля с киля
            ship_y = self.keel_ship.y

            if self.orient_ship == 0: #если ориентация корабля по оси Х
                ship_x += i #то шагаю по координатам Х

            if self.orient_ship == 1: #если ориентация корабля по оси У
                ship_y += i #то шагаю по координатам У

            ship_dots.append(Dot(ship_x, ship_y)) #Добавляю полученную координату в список точек корабля


        return ship_dots #Возвращаю список точек

    # метод проверки попаданий
    def shooten(self, shot):
        return shot in self.dots


class Board:
# Класс описывающий методы и атрибуты игрового поля
    def __init__(self, hid=False, size=6):
        self.hid = hid  # пользователь или компьютер
        self.size = size # размер поля

        self.count = 0 # счетчик

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def out(self, d): #метод проверки в рамках поля координаты или нет
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def add_ship(self, ship): #метод добавления корабля на игровое поле

        for d in ship.dots: #проходим по точкам корабля, для проверки
            if self.out(d) or d in self.busy: #если точка за пределами поля или занята
                raise BoardWrongShipException() #вызываем исключение
        for d in ship.dots: #исключени не произошло
            self.field[d.x][d.y] = "■" #заполняем точки символом квадратика
            self.busy.append(d) #добавляем точки в список занятых

        self.ships.append(ship) #добавляем точки корабля в список кораблей на поле
        self.contour(ship) # отмечаем контуры корабля, по одной клетке вокруг корабля, как занятые




    def contour(self, ship, verb=False): #метод прорисовки контуров корабля
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ] # список координат точек, окружающих конкретную точку
        for d in ship.dots: #пошагово получаем все точки вокруг точки корабля
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy: #если точка не за пределами поля или не занята
                    if verb:
                        self.field[cur.x][cur.y] = "." #контуры помечаются символом "."
                    self.busy.append(cur) #точку добавляем в занятые

    def __str__(self): # вывод игрового поля на экран
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid: #если игровое поле Компьютера, то символы корабля меняю на "О"
            res = res.replace("■", "O")
        return res

    def shot(self, d): #метод выстрела
        if self.out(d): #если выстрел за пределы поля,
            raise BoardOutException() #то вызываем соответствующее исключение

        if d in self.busy: #если выстрел по одной и той же точке, то
            raise BoardUsedException() #вызываем соответствующее исключение

        self.busy.append(d) #если исключения не вызваны, то точка выстрела добавлена в список занятых точек

        for ship in self.ships:#сверяем координаты выстрела с координатами точек каждоного корабля
            if d in ship.dots:#если координаты точки выстрела совпадает с одной из точек корабля
                ship.health -= 1 #отнимаем единицу от здоровья корабля
                self.field[d.x][d.y] = "X" #координату выстрела помечаем символом "Х"
                if ship.health == 0: #если здоровья не осталось, корабль уничтожен
                    self.count += 1 #прибавляем счетчик потопленных кораблей
                    self.contour(ship, verb=True) #обрисовываем контур корабля по одной клетки вокруг
                    print("Корабль уничтожен!")
                    return False #выстрел больше не нужен
                else:
                    print("Корабль поврежден!")
                    return True #еще выстрел

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []


class Player:
    # класс игрок, общий для пользователя и компьютера
    def __init__(self, board, enemy): # получает две игровые доски - свою и противника
        self.board = board
        self.enemy = enemy

    def ask(self): # метод запроса выстрела у пользователя, реализовывается в объекте потомке
        raise NotImplementedError()

    def move(self):#метод осуществляет ход
        while True:
            try: # отслеживаем исключения при выстреле
                target = self.ask()# запрашиваем у игрока координаты выстрела
                repeat = self.enemy.shot(target) #нужен ли повторный выстрел, в случае повреждения корабля
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    # Объект игрок - компьютер
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5)) #выбираем точку со случайными координатами
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    # Объект игрок - пользователь
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()
            if len(cords) != 2:
                print(" Введите 2 координаты через пробел! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    # Основной класс игры
    def __init__(self, size=6):
        self.size = size # размер доски
        # возможность ручного ввода координат корабля
        self.greet()
        if input("Хотите разместить корабли вручную? 'Y' - Да, 'N' - Нет: ") == 'y':
            pl = self.manual_board()  # доска пользователя, вручную
        else:
            pl = self.random_board() #доска пользователя, случайная
        co = self.random_board() #доска компьютера случайная
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def manual_board(self):
        board = None
        while board is None:
            board = self.manual_place()
        return board

    def random_place(self): # Размещение кораблей в случайном порядке
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def ask(self, l): # метод запроса и проверки координат начальной точки корабля, при ручном вводе
        self.l = l
        while True:
            cords = input(f" Введите координаты носа корабля, размером - {l}, через пробел: ").split()
            if len(cords) != 2:
                print(" Введите 2 координаты через пробел! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)
    def manual_place(self): # Размещение кораблей вручную пользователем
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        for l in lens:
            keel_sheep1 = self.ask(l)
            if l == 1:
                orient_sheep = '0'
            else:
                orient_sheep = input("Расположение корабля: 0 - вертикальное, 1 - горизонтальное: ")
                if not (orient_sheep.isdigit()):
                    print(" Введите число! ")
                    continue
            ship = Ship(keel_sheep1, l, int(orient_sheep))
            try:
                board.add_ship(ship) # добавляем новый корабль в список кораблей
                print("-" * 20) # выводим доску игрока с целью демонстрации изменений
                print("Доска пользователя:")
                print(board)
                print("-" * 20)
            except BoardWrongShipException:
                pass
        board.begin()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1 #если требуется повторный ход, счетчик остается прежним

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.loop()



g = Game()
g.start()


