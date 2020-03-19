# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию. И получить объект: словарь из предыдущего задания.
import pickle
import json

with open('group.pickle', 'rb') as f:
    group_pickle = pickle.load(f)


with open('group.json', 'r', encoding='utf-8') as f:
    group_json = json.load(f)

print(group_json)
print(group_pickle)