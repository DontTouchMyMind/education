# Семейная пара собирается в отпуск
# каждый из супругов собирает вещи
# Мах взял эти вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла эти вещи
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# Какие вещи взяли супруги?
print(max_things | kate_things)
# Найти повторяющиеся вещи?
print(max_things & kate_things)
# Какие вещи взял Макс, но не взяла Кэйт
print(max_things - kate_things)
# Какие вещи взяла Кейт, но не взял Макс
print(kate_things - max_things)
