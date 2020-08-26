# f = open(r'C:/file.txt', 'v')
from typing import Literal, Final, final, Dict, Any, TypedDict


def open_file(file, mode):
    pass


f = open_file(r'C:/file.txt', 'v')


def open_file_modify(file, mode: Literal['r', 'w']):  # Мы можем ограничить набор значений для mode.
    pass


var = open_file_modify(r'C:/file.txt', 'v')

# Создание констант.
pi: Final = 3.14

pi = 1


# Закрытые, "запечатанные" классы (запритит наследование).
@final
class Dog:
    def __init__(self):
        self.paws = 4
        self.health = 100
        self.sound = 'woof-woof'

    def bark(self):
        print(self.sound)


class SuperDog(Dog):
    def __init__(self):
        super().__init__()
        self.health = 200
        self.sound = 'super-woof'


# dog = SuperDog()
# print(dog.health)
# dog.bark()

# Объявление словарей.
person: Dict[str, str] = {'name': 'John', 'last_name': 'Conrad', 'sex': 'm'}

dict_result: Dict[str, Any] = {'word': 'hello', 'count': 5, 'comment': 'a very interesting word'}
dict_result['comment'] = 123  # Можем записать другой тип данных, т.к. объявили Any.
print(dict_result['lol'])  # Можем даже обратиться к несуществующему ключу.


# В Python 3.8 мы можем прикрыть эти "проблемы".
class WorldStat(TypedDict):
    word: str
    count: int
    comment: str


dict_result: WorldStat = {'word': 'hello', 'count': 5, 'comment': 'a very interesting word'}
dict_result: WorldStat = {'word': 'hello', 'comment': 'a very interesting word'}
print(dict_result['lol'])
