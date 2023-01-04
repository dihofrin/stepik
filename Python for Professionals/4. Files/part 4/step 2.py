"""
https://stepik.org/lesson/623073/step/2?unit=618703

Дополните приведенный ниже код, чтобы он преобразовал словарь words в строку в формате JSON, пропуская пары, которые имеют недопустимые ключи, и присвоил полученный результат переменной data_json.

Примечание. Используйте необязательный аргумент skipkeys.
"""

import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.dumps(words, skipkeys=True)