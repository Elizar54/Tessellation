import turtle as t
import math
raw_coords = []
t.speed(10)


def get_num_hexagons():
    try:
        num = int(input('Введите число шестиугольников, располагаемых в ряд, от 4 до 20 включительно: '))

        if num >= 4 and num <= 20:
            return num
        else:
            print('Число должно быть от 4 до 20')
            get_num_hexagons()

    except ValueError:
        print('Ошибка, введите число.')
        get_num_hexagons()


def get_color_choice():
    color_list = ['красный', 'синий', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
    print('Допустимые цвета заливки:')

    for color in color_list:
        print(color)
    color = input('Пожалуйста, введите цвет: ')
    if color in color_list:
        if color == 'красный':
            color = 'red'
        elif color == 'синий':
            color = 'blue'
        elif color == 'желтый':
            color = 'yellow'
        elif color == 'оранжевый':
            color = 'orange'
        elif color == 'пурпурный':
            color = 'purple'
        elif color == 'розовый':
            color = 'pink'
        return color
    else:
        print('Цвет введен неверно!')
        print()
        get_color_choice()


def draw_hexagon(x, y, side_len, color_fill):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.rt(90)

    for move in range(6):
        if move == 2:
            x_second, y_second = t.xcor(), t.ycor()
            raw_coords.append(x_second)
            raw_coords.append(y_second)
        t.color(color_fill, color_fill)
        t.forward(side_len)
        t.rt(60)
    
    t.lt(90)
    t.end_fill()

# временный квадрат
t.up()
t.goto(-250, 250)
t.down()
for i in range(4):
    t.forward(500)
    t.rt(90)

quant_of_hexes = get_num_hexagons()
filling_color_1 = get_color_choice()
filling_color_2 = get_color_choice()
small_diagonal = 500 // quant_of_hexes
side_len = small_diagonal / math.sqrt(3)
x = -250 + small_diagonal
y = 250

for i in range(quant_of_hexes):
    for hex in range(quant_of_hexes):
        if hex % 2 != 0:
            draw_hexagon(x, y, side_len, filling_color_1)
        else:
            draw_hexagon(x, y, side_len, filling_color_2)
        x += 2 * side_len * math.sin(math.pi / 3)
    t.up()  # закончил рисовать ряд

    if i % 2 == 0:
        raw_coords = raw_coords[:2]
        x, y = raw_coords[0], raw_coords[1]
        raw_coords.clear()
    else:
        raw_coords = raw_coords[2:4]
        x, y = raw_coords[0], raw_coords[1]
        raw_coords.clear()
    
t.mainloop()


    

