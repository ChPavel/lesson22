# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, condition: str, direction: str):
        self.__condition = condition
        self.__direction = direction

    def __self_speed(self) -> float:
        if self.__condition == 'fly':
            return 1.2
        elif self.__condition == 'crawl':
            return 0.5
        else:
            raise ValueError("Я умею только 'fly' и 'crawl', выше головы не прыгаю!")

    def __coordinate_generator(self):
        s = self.__self_speed()
        motion_coordinates = {'UP': [0, s], 'DOWN': [0, -s], 'LEFT': [-s, 0], 'RIGTH': [s, 0]}

        if self.__direction in ['UP', 'DOWN', 'LEFT', 'RIGTH']:
            return motion_coordinates[self.__direction]
        else:
            raise ValueError("Я всё время в движении ('UP', 'DOWN', 'LEFT', 'RIGTH'), покой мне только снится!")

    def move(self, field, x_coord, y_coord):
        x_change, y_change = self.__coordinate_generator()

        new_y = y_coord + y_change
        new_x = x_coord + x_change

        field.set_unit(x=new_x, y=new_y, unit=self)


#     def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed=1):
#
#         if is_fly and crawl:
#             raise ValueError('Рожденный ползать летать не должен!')
#
#         if is_fly:
#             speed *= 1.2
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#         if crawl:
#             speed *= 0.5
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#
#             field.set_unit(x=new_x, y=new_y, unit=self)
#
# #     ...
