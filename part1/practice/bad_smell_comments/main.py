# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, field_x, field_y, direction, flying, crawling, speed = 1):
        """Функция реализует перемещение юнита по полю. В качестве параметров принимает его текущие координаты, 
        состояние (летит или крадется), направление движения с базовым параметр скорости.
        :param field: поле по которому перемещается юнит
        :param field_x: x-координата
        :param field_y: у- координата
        :param direction: направление перемещения
        :param flying: состояние - летит
        :param crawling : состояние - крадется
        :param speed: базовый параметр скорости
        """
        if flying and crawling:
            raise ValueError('Рожденный ползать летать не должен!')

        if flying:
            speed *= 1.2
            if direction == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed
        if crawling :
            speed *= 0.5
            if direction == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
