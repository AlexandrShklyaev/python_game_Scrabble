from random import randint


def get_new_letters(list_alfa, count_alfa):
    """
    Функция для случайного выбора букв из данного списка букв (учтена возможность выпадания одинаковых букв)
    :param list_alfa: данный список букв
    :param count_alfa: количество букв
    :return: (список выбранных букв ["буква1",...], данный список букв без выбранных букв ["буква2",...])
    """
    append_alfa = []
    for each_elem in range(count_alfa):  # проходим циклом по количеству букв
        ind = randint(0, len(list_alfa) - 1)  # выбираем индекс елемента списка букв случайным образом
        append_alfa.append(list_alfa[ind])  # формируем копию данного списка букв
        list_alfa.remove(list_alfa[ind])  # удаляем выбранную букву
    return append_alfa, list_alfa


def get_words() -> list:
    """
    Функция открыввает файл со словами и возвращает список из них
    :return: ["слово1","слово2",...]
    """
    with open("russian_word.txt", "r", encoding="utf-8") as file_words:
        return [each_elem.strip() for each_elem in file_words.readlines()]  # цикл по всем строкам файла


def get_dict_letters():
    """
    Фунцкция возвращает словарь с количеством и ценностью букв
    :return: {"буква1":[количество1,ценность1],...}
    """
    dict_alfa = {"а": [8, 1], "б": [2, 3], "в": [4, 1], "г": [2, 3], "д": [4, 2], "е": [8, 1], "ё": [1, 3],
                 "ж": [1, 5], "з": [2, 5], "и": [5, 1], "й": [1, 4], "к": [4, 2], "л": [4, 2], "м": [3, 2],
                 "н": [5, 1], "о": [10, 1], "п": [4, 2], "р": [5, 1], "с": [5, 1], "т": [5, 1], "у": [4, 2],
                 "ф": [1, 10], "х": [1, 5], "ц": [1, 5], "ч": [1, 5], "ш": [1, 8], "щ": [1, 10], "ъ": [1, 10],
                 "ы": [2, 4], "ь": [2, 3], "э": [1, 8], "ю": [1, 8], "я": [2, 3]}
    return dict_alfa


def get_list_dict(dict_alfa):
    """
    Функция преобразует словарь букв в список букв, учитывая их количество
    :param dict_alfa: словарь букв
    :return: ["буква1","буква1","буква2",...]
    """
    new_list = []
    for each_elem in dict_alfa:  # для каждой буквы из словаря
        for count_letters in range(dict_alfa[each_elem][0]):  # цикл по количеству текущей буквы
            new_list.append(each_elem)
    return new_list


def get_new_list_letters(user_word, user_list_letters):
    """
    Функция удаляет буквы слова из списка букв, если все буквы слова присутствуют в списке, иначе вернет исходный список
    :param user_word: слово
    :param user_list_letters: список букв
    :return: ["буква1", "буква2"]
    """
    list_alfa = []
    for each_elem in user_list_letters:  # создаем копию списка
        list_alfa.append(each_elem)
    for each_elem in user_word:  # цикл по всем буквам слова
        if each_elem not in user_list_letters:  # если буквы нет в списке
            return user_list_letters  # возвращаем исходый список
        else:
            list_alfa.remove(each_elem)  # удаляем из копии текущую букву
    return list_alfa


def get_init_users(list_letters):
    """
    Инициализация игроков и их списков букв
    :param list_letters: данный список букв
    :return: список букв, ["имя игрока1","имя игрока2"], [[список букв игрока 1], [список букв игрока 2]]
    """
    user_letters = [[], []]
    user_letters[0], list_letters = get_new_letters(list_letters, 7)  # список букв игрока 1
    user_letters[1], list_letters = get_new_letters(list_letters, 7)  # список букв игрока 2

    print("Привет.\nМы начинаем играть в Scrabble")
    user_name = [input("Введите имя 1-го игрока: "), input("Введите имя 2-го игрока: ")]
    print(f"{user_name[0]} vs {user_name[1]}")
    print("-" * 20)
    print(f"Буквы игрока {user_name[0]}: {user_letters[0]}")
    print(f"Буквы игрока {user_name[1]}: {user_letters[1]}")
    return list_letters, user_name, user_letters


def get_score(word, dict_alffa):
    """
    Функция возвращает стоимость слова из словаря вида {"буква":[количество, стоимость]}
    """
    score = 0
    for each_letter in word:
        score += dict_alffa[each_letter][1]
    return score


def game():
    """
    Основной код программы
    :return: список игроков, список очков игроков
    """
    users_words = []  # список придуманных слов
    total_score = [0, 0]  # список очков игроков
    list_words = get_words()  # список возможных слов

    dict_letters_base = get_dict_letters()  # словарь букв
    list_letters_base = get_list_dict(dict_letters_base)  # список букв из словаря
    list_letters, user_name, user_letters = get_init_users(list_letters_base)  # инициализация игроков и их букв

    step = 0
    while (len(list_letters) + len(user_letters[0]) + len(user_letters[1])) > 0:  # пока хоть один список букв не пуст
        numb_user = step % 2  # вычисляем номер игрока
        step += 1
        if not numb_user:  # выводим номер раунда для пары игроков
            print("- " * 15, "РАУНД", 1 + step // 2, " -" * 15)
        # вывод букв игрока и ввод слова
        word = input(f"Ходит -{user_name[numb_user]}-. Придумайте слово, используя буквы: {user_letters[numb_user]}: ")
        word2 = word.replace("ё", "е")  # обработка буквы ё
        if word == "stop":  # остановка игры по кодовому слову
            break

        if word in users_words or word2 in users_words:  # было ли уже такое слово
            print(" " * 3, "Такое слово уже было! Попробуйте ещё раз")
            step -= 1
            continue  # даём игроку еще шанс
        else: # такого слова еще не было

            if word in list_words or word2 in list_words:  # есть ли слово в файле
                new_list_letters = get_new_list_letters(word, user_letters[numb_user])
                if user_letters[numb_user] == new_list_letters:  # использовал не только свои буквы
                    new_alfa, list_letters = get_new_letters(list_letters, 1)  # получим 1 букву
                    print(" " * 3, "Слово нужно составлять из своих букв!")
                else:  # использовал свои буквы
                    new_alfa, list_letters = get_new_letters(list_letters, len(word) + 1)  # получим буквы +1
                    print(" " * 3, "Есть такое слово!", end="")
                    users_words.append(word)  # добавим слово в списов использованных слов
                    total_score[numb_user] += get_score(word, dict_letters_base)  # увеличим очки игрока
                    print(f" Ваши очки увеличены на {get_score(word, dict_letters_base)}.")
                for each in new_alfa:
                    new_list_letters.append(each)
                user_letters[numb_user] = new_list_letters  # обновим список букв игрока
            else:  # нет такого слова в файле
                new_alfa, list_letters = get_new_letters(list_letters, 1)  # получим 1 букву
                print(" " * 3, "Такого слова нет!", end="")
                user_letters[numb_user].append(new_alfa[0])  # добавим 1 букву в список букв игрока

            print(" " * 3, f"Вам добавлены буквы: {new_alfa}")
    return user_name, total_score


def print_statistik(users_name, totals_score):
    """
    Вывод результатов игры
    :param users_name: список игроков
    :param totals_score: список очков
    :return: -
    """
    print("~" * 10)
    if totals_score[0] > totals_score[1]:
        print("Выигрывает", users_name[0])
    elif totals_score[0] < totals_score[1]:
        print("Выигрывает", users_name[1])
    else:
        print("У вас ничья!")
    print(f"Счет {totals_score[0]}:{totals_score[1]}")


if __name__ == "__main__":
    # основная программа
    users_name, totals_score = game()
    print_statistik(users_name, totals_score)
