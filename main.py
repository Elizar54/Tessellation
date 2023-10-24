import turtle as t
import math

def get_num_hexagons():
    try:
        num = int(input('Введите число шестиугольников, располагаемых в ряд, от 4 до 20 включительно: '))

        if num >= 4 and num <= 20:
            return num
        else:
            print('Оно должно быть от 4 до 20')
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
        t.color(color_fill, color_fill)
        t.forward(side_len)
        t.rt(60)
    
    t.lt(90)
    t.end_fill()


quant_of_hexes = get_num_hexagons()
filling_color_1 = get_color_choice()
filling_color_2 = get_color_choice()
x = 2
y = 2

for i in range(2):
    for hex in range(quant_of_hexes):
        if hex % 2 != 0:
            draw_hexagon(x, y, 20, filling_color_1)
        else:
            draw_hexagon(x, y, 20, filling_color_2)
        x += 2 * 20 * math.sin(math.pi/3)
    t.up()
    t.goto(x - (quant_of_hexes - 1) * 20 * math.sin(math.pi/3), y)
    t.goto(x - (quant_of_hexes - 1) * 20 * math.sin(math.pi/3), y + 3 * 20 * math.cos(math.pi/3) + 20)

    x = x - (quant_of_hexes - 1) * 20 * math.sin(math.pi/3)
    y = y + 3 * 20 * math.cos(math.pi/3) + 20
t.done()

    

