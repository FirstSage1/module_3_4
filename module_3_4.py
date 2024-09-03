# ДЗ. Модуль 3_4.Произвольное число параметров.
# ===================================================
def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.find(i):
            same_words.append(i)
        if i.find(root_word):
            same_words.append(root_word)
        return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# konsol1=['richiest', 'orichalcum', 'richies']
# konsol2=['Able', 'Disable']
