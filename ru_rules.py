# -*- coding: utf-8 -*-

vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщьъ"
signs_of_softness = "ьъ"
vocabulary = "аеёиоуыэюябвгджзйклмнпрстфхцчшщьъ1234567890 -,.:;!?#№$%&€"


def apply_the_rules(words):
    for i in range(len(words)):
        last_consonant = False
        last_vowel = False

        # солнце
        words[i] = words[i].replace('лнц', 'нц')
        # явства
        words[i] = words[i].replace('вств', 'ств')
        # лестница
        words[i] = words[i].replace('стн', 'сн')
        words[i] = words[i].replace('стл', 'сл')
        words[i] = words[i].replace('здн', 'зн')
        # сердце
        words[i] = words[i].replace('рдц', 'рц')
        words[i] = words[i].replace('рдч', 'рч')
        words[i] = words[i].replace('стц', 'сц')
        words[i] = words[i].replace('здц', 'зц')
        # агентские
        words[i] = words[i].replace('нтск', 'нск')
        words[i] = words[i].replace('ндск', 'нск')
        words[i] = words[i].replace('ндц', 'нц')
        # предантство
        words[i] = words[i].replace('нтств', 'нств')
        # абстракционистский
        words[i] = words[i].replace('стск', 'ск')
        # счастье
        words[i] = words[i].replace('сч', 'щ')
        # премудрая
        if len(words[i]) > 3 and words[i][:3] == 'пре' and (words[i][3] in consonants or words[i][3] in vowels):
            words[i] = 'при' + words[i][3:]
        if len(words[i]) > 1:
            # порог
            if words[i][len(words[i]) - 1] == 'г':
                words[i] = words[i][:len(words[i]) - 1] + 'к'
            # дуб
            elif words[i][len(words[i]) - 1] == 'б':
                words[i] = words[i][:len(words[i]) - 1] + 'п'
            # Крылов
            elif words[i][len(words[i]) - 1] == 'в':
                words[i] = words[i][:len(words[i]) - 1] + 'ф'
            # Крылов
            elif words[i][len(words[i]) - 1] == 'д':
                words[i] = words[i][:len(words[i]) - 1] + 'т'
            # Крылов
            elif words[i][len(words[i]) - 1] == 'ж':
                words[i] = words[i][:len(words[i]) - 1] + 'ш'
            # Крылов
            elif words[i][len(words[i]) - 1] == 'з':
                words[i] = words[i][:len(words[i]) - 1] + 'с'

        stressed = False
        for j in range(len(words[i])):
            if words[i][j] == '\'':
                stressed = True
                break

        if stressed:
            for j in range(len(words[i])):
                curr_letter = words[i][j]
                if last_consonant and last_vowel and words[i][j] in consonants:
                    if words[i][j - 1] == 'о':
                        words[i] = words[i][:j - 1] + 'а' + words[i][j:]
                    if words[i][j - 1] == 'е':
                        words[i] = words[i][:j - 1] + 'и' + words[i][j:]
                    last_vowel = False

                if curr_letter in consonants:
                    last_consonant = True
                    continue
                if curr_letter in vowels:
                    last_vowel = True
                    continue
    return words
