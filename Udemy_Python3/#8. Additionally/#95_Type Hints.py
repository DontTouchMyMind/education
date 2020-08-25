import random
from typing import Optional, Any, Union, List, Tuple, Dict, Iterable


class Character:

    def __init__(self, armor: int, power: int):
        self.armor = armor
        self.power = power
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0


# c1 = Character('bad day', 'even worse')     # Мы можем совершить ошибку в runtime.
# Что бы такого избежать мы можем прописывать ожидаемые типы в момент декларации.
# После добавления armor: int, power: int линтер сразу подсветит неверные данные,
# при создании объекта класса Character.
c1 = Character(10, 20)  # Класс Character получает ожидаемые типы.
c1.hit(20)

# Иногда нам необходимо объявить тип int, но по умоч. установить None.
amount: int
amount = None

price: Optional[int]
price = 10
price = None
price = 'asd'  # Ошибка присваивания!

# Если в коде уже используются type hint's, то необходимо явно указать тип,
# даже если тип может быть любой!
attack: Any = 1
attack = 'hi'  # Ошибки присваивания не будет.

# Также возможно указать объединение типов (int и float).
length: Union[int, float]
length = 1
length = 2.5  # Ошибки присваивания не будет.
length = 'asdf'  # Ошибка присваивания!

quotes: list  # Но мы не указали какого именно типа должны быть переменные в списке.
quotes = 'abcd'

quotes: List[int]  # Анологично с Set, FrozenSet.
quotes.append(1)
quotes.append('asdf')  # Ошибка присваивания!

player: Tuple[str, int] = ('Kramnik', 2750)

# Если мы хотим показать, что кортеж состоит из множества элементов одного типа.
changes_in_rating: Tuple[int, ...]
changes_in_rating = (1, 2, 3, 4, 5)
changes_in_rating = (1, 'qweq')  # Ошибка присваивания!

# Можно декларировать словарь.
chess_player: Dict[str, int] = {'Kramnik': 2750}  # DefaultDict также доступен.


# Указать можно не только тип входящих переменных, но и возвращаемый функцией тип.
# def is_alive(self) -> bool:

# Что бы указать, что из функции возвращается некий итерируемый объект.
def random_stream(min_val: int, max_val: int) -> Iterable[int]:
    while True:
        yield random.randint(min_val, max_val)
