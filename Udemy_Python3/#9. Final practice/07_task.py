# Давайте попробуем запрограммировать одну известную игру "Виселица" (без рисования).
#
# Смысл игры: компьютер генерирует слово из словаря,
# а человек побуквенно пытается угадать, что за слово было загадано.
# Количество попыток назвать букву ограничено.
# Если количество попыток превышено, то игрок проигрывает, если открыл всё слово - победил.
#
# Требования к реализации:
#
# Завести класс, отвечающий за логику игры, который:
#   - позволяет настраивать кол-во позволенных ошибок (API принимает соответствующий параметр)
#   - позволяет клиентскому коду запрашивать генерацию слова
#   - позволяет клиентскому коду передавать в логику догадку игрока (передача буквы)
#   - позволяет клиентскому коду запрашивать:
#     -- кол-во оставшихся попыток
#     -- строку показывающую какие буквы открыты, а какие скрыты
#     (если буква скрыта вместо неё ставим подчёркивание или дефис), т.е., по сути, текущее состояние игры
#     -- отсортированные буквы, которые игрок уже называл (вводил)
#
# Клиентский код организует цикл в котором пользуется API класса,
# который реализует логику игры, и выводит все необходимые строки для общения с игроком,
# показывает текущее состояние игры, поздравляет с победой и уведомляет о поражении.
#
# Файл со словами прикреплён к лекции. Читать можно в кодировке UTF8.
import random


class Game:

    def __init__(self, try_number: int):
        self.number = 1
        self.try_number = try_number
        self.game_word = []
        self.letter = ''
        self.attempts = 1
        self.remaining_attempts = self.try_number - self.attempts
        self.player_word = []

    def get_word(self):
        with open(r'/media/WorkSpace/Project/Python/git'
                  r'/education/Udemy_Python3/'
                  r'#9. Final practice/WordsStockRus.txt', 'r') as file:
            lines = file.readlines()
        self.game_word = list(lines[random.randint(0, 11650)])[:-1]
        return self.game_word

    def make_try(self, input_letter):
        self.attempts += 1
        self.player_word.append(input_letter)
        self.letter = input_letter

    def already_used_letter(self):
        return sorted(set(self.player_word))

    def get_visible_word(self):
        return list(letter if letter in self.player_word else '_' for letter in self.game_word)


# 1. Запрос уровня сложности
# 2. Запуск и инициализация игры,
# 3. Генерация слова
# 4. Запуск цикла
#       Проверка победителя
#       Вывод букв которые игрок назвал
#       Запрос буквы
#       Вывод результата
#       Вывод кол-ва оставшихся попыток

difficult = input('Enter number of attempts: ')

g = Game(int(difficult))

g.get_word()

while True:
    if g.player_word == g.game_word:
        print('Congratulations! You are winner!')
        play_more = input('Do you want play more? (say "yes" or "no"): ')
        if play_more == 'yes':
            g.game_word()
        else:
            break
    print(g.already_used_letter())
    g.make_try(input('Enter your letter: '))
    print(g.get_visible_word())
    print(g.remaining_attempts)
