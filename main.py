import turtle

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
        return color
    else:
        print('Цвет введен неверно!')
        print()
        get_color_choice()

