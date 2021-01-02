# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1,
# Two — 2,
# Three — 3,
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from google_trans_new import google_translator as Translator
# долго пытался сделать пример с обычным модулем от google, но была ошибка:
# 'NoneType' object has no attribute 'group'
# Нашел вот тут решение проблемы:
# https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group


with open('lesson_5_task_4.txt', encoding='utf-8') as f:
    contents = f.read()

translator = Translator()
result = translator.translate(contents, lang_src='en', lang_tgt='ru')
# единственный минус - записывает результат в одну строчку
# Результат
# Один - 1  Два - 2  Три - 3  Четыре - 4

result = result.replace('  ', '\n')  # Поэтому приходится делать переносы вручную
with open('lesson_5_task_4_result.txt', 'w', encoding='utf-8') as f:
    f.write(result)
