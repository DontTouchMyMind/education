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

    def __init__(self, attempts: int):
        self.attempts = attempts
        self.game_word = []
        self.letter = ''
        self.player_word = []

    def request_word(self):
        with open(r'/media/WorkSpace/Project/Python/git'
                  r'/education/Udemy_Python3/'
                  r'#9. Final practice/WordsStockRus.txt', 'r') as file:
            # with open(r'/home/belousov/My_Proj/education/Udemy_Python3/#9. Final practice/WordsStockRus.txt', 'r') as file:
            lines = file.readlines()
        self.game_word = list(lines[random.randint(0, 11650)].strip())  # .strip() - удалит \n, аналогично [:-1]
        return self.game_word

    def make_attempt(self, input_letter):
        self.player_word.append(input_letter)
        self.letter = input_letter
        if input_letter not in self.game_word:
            self.attempts -= 1

    def already_used_letter(self):
        return sorted(self.player_word)

    def get_visible_word(self):
        return list(letter if letter in self.player_word else '_' for letter in self.game_word)


difficult = input('Enter number of attempts: ')

g = Game(int(difficult))

g.request_word()

while g.attempts != 0:
    if g.get_visible_word() == g.game_word:
        print('Congratulations! You are winner!')
        play_more = input('Do you want play more? (say "yes" to continue playing! ): ')
        if play_more == 'yes':
            g.player_word = []
            g.request_word()
        else:
            break
    print(g.get_visible_word())
    g.make_attempt(input('Enter your letter: '))
    print(f'You already used - {g.already_used_letter()}')
    print(f'You have {g.attempts} attempts left.')

else:
    print('Sorry! You lose! You have no attempts left.')
    print(f'The hidden word was {g.game_word}')

print('Goodbye! See you soon!')
