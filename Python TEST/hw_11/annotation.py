"""
Задача 1. Класс МояСтрока
"""


class MyStr(str):
    """
    Класс МояСтрока, наследуется от str.
    Добавляет атрибуты author_name и creation_time.
    """

    def __new__(cls, value, author_name):
        obj = super().__new__(cls, value)
        obj.author_name = author_name
        obj.creation_time = datetime.now()
        return obj

    def __str__(self):
        return f'{self} (author: {self.author_name}, creation time: {self.creation_time})'


print(MyStr('test', 'John'))

"""
Задача 2. Класс Архив 
"""


class Archive:
    """
    Класс Архив хранит архив чисел и строк в списках.
    При создании нового экземпляра, данные добавляются в архив.
    """

    nums_archive = []
    strs_archive = []

    def __init__(self, num, text):
        self.num = num
        self.text = text
        Archive.nums_archive.append(num)
        Archive.strs_archive.append(text)

    def __str__(self):
        return f'Число: {self.num}, текст: {self.text}'


arc = Archive(5, 'hello')
print(arc)

"""
Задача 4. Класс Архив с методами вывода

Класс Архив хранит архив чисел и строк в списках.
При создании нового экземпляра, данные добавляются в архив.

Добавлены методы:

- __str__ - для вывода информации для пользователя 
- __repr__ - для вывода отладочной информации
"""


class Archive:
    nums_archive = []
    strs_archive = []

    def __init__(self, num, text):
        self.num = num
        self.text = text
        Archive.nums_archive.append(num)
        Archive.strs_archive.append(text)

    def __str__(self):
        # Выводим информацию для пользователя
        return f'Число: {self.num}, текст: {self.text}'

    def __repr__(self):
        # Выводим информацию для разработчика
        return f'Archive(num={self.num}, text="{self.text}")'


"""    
Задача 5. Класс Прямоугольник
"""


class Rectangle:
    """
    Класс Прямоугольник реализует сложение и вычитание экземпляров.
    При этом складываются и вычитаются периметры фигур.
    """

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def __add__(self, other):
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_a}, {self.side_b}'


"""
Задача 6. Сравнение прямоугольников   
"""


class Rectangle:
    def __init__(self, side_a, side_b=0):

    # код __init__

    def get_area(self):
        return self.side_a * self.side_b

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.side_a}, {self.side_b}'

    def __repr__(self):
        return f'Rectangle(side_a={self.side_a}, side_b={self.side_b})'
