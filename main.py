import turtle as t
import math

raw_coords = []
t.speed(15)


def get_num_hexagons():
    num = 0
    error_cnt = 0

    while not (4 <= num <= 20) or not str(num).isdigit():

        if error_cnt > 0:
            print('Ошибка: число должно быть от 4 до 20 и записано в численной форме.')

        num = input('Введите число шестиугольников, располагаемых в ряд, от 4 до 20 включительно: ')

        if num.isdigit():
            num = int(num)
        else:
            num = 0
        error_cnt += 1
    else:
        return num

def get_color_choice():
    color_dict = {'красный': 'red', 'синий': 'blue', 'желтый': 'yellow', 'оранжевый': 'orange', 
                  'пурпурный': 'purple', 'розовый': 'pink'}
    error_cnt = 0
    color_choice = ''
    print('Допустимые цвета заливки:')

    for color in color_dict.keys():
        print(color)

    while color_choice not in color_dict.keys():
        if error_cnt > 0:
            print('Цвет введен неверно.')

        color_choice = input('Пожалуйста, введите цвет: ').lower()
        error_cnt += 1
    else:
        print()
        return color_dict[color_choice]


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
        t.color('black', color_fill)
        t.forward(side_len)
        t.rt(60)
    
    t.lt(90)
    t.end_fill()

# временный квадрат - не забудь убрать)
t.up()
t.goto(-250, 250)
t.down()
for i in range(4):
    t.forward(500)
    t.rt(90)

quant_of_hexes = get_num_hexagons()
filling_color_1 = get_color_choice()
filling_color_2 = get_color_choice()
print('Наслаждайтесь:)')

small_diagonal = 500 // quant_of_hexes
side_len = small_diagonal / math.sqrt(3)
x = -250 + small_diagonal
y = 250

for row in range(quant_of_hexes):
    for hex in range(quant_of_hexes):
        if hex % 2 != 0:
            draw_hexagon(x, y, side_len, filling_color_1)
        else:
            draw_hexagon(x, y, side_len, filling_color_2)
        x += 2 * side_len * math.sin(math.pi / 3)
    t.up()  # закончил рисовать ряд - красава!

    if i % 2 == 0:
        raw_coords = raw_coords[:2]
        x, y = raw_coords[0], raw_coords[1]
        raw_coords.clear()
    else:
        raw_coords = raw_coords[2:4]
        x, y = raw_coords[0], raw_coords[1]
        raw_coords.clear()
    
t.mainloop()
