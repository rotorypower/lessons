"""Напишите программу, которая принимает текст и
выводит два слова: наиболее часто встречающееся и самое длинное.
"""

import collections

text = (
    'Mercedes-Benz W202 — компактный представительский легковой автомобиль немецкого автопроизводителя '
    'Mercedes-Benz из серии С-класса. Пришёл на смену модели W201 '
    '(также известной как Mercedes-Benz 190) в мае 1993 года. '
    'До появления A-класса в 1997 году оставался стартовой моделью компании.'
)
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print("Часто встречаемое слово : " + most_common)
print("Самое длинное слово : " + longest)
