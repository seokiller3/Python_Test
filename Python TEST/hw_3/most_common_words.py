import re
from collections import Counter

text = "В большой текстовой строке, подсчитать количество встречаемых слов! Не учитывать знаки препинания и Регистр " \
       "Символов? Вернуть 10 самых частых. Большой, текстовой, строке, подсчитать!"

top_10_words = Counter(re.sub(r'[^\w\s]', '', text.lower()).split()).most_common(10)
print(top_10_words)
