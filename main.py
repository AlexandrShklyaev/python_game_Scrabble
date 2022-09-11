from random import randint


def get_new_letters(list_alfa, count_alfa):
    append_alfa = []
    for each_elem in range(count_alfa):
        ind = randint(0, len(list_alfa) - 1)
        append_alfa.append(list_alfa[ind])
        list_alfa.remove(list_alfa[ind])
    return append_alfa, list_alfa


def get_words() -> list:
    with open("russian_word.txt", "r", encoding="utf-8") as file_words:
        return [each_elem.strip() for each_elem in file_words.readlines()]


def get_dict_letters():
    dict_alfa = {"а": [8, 1], "б": [2, 3], "в": [4, 1], "г": [2, 3], "д": [4, 2], "е": [8, 1], "ё": [1, 3],
                 "ж": [1, 5], "з": [2, 5], "и": [5, 1], "й": [1, 4], "к": [4, 2], "л": [4, 2], "м": [3, 2],
                 "н": [5, 1], "о": [10, 1], "п": [4, 2], "р": [5, 1], "с": [5, 1], "т": [5, 1], "у": [4, 2],
                 "ф": [1, 10], "х": [1, 5], "ц": [1, 5], "ч": [1, 5], "ш": [1, 8], "щ": [1, 10], "ъ": [1, 10],
                 "ы": [2, 4], "ь": [2, 3], "э": [1, 8], "ю": [1, 8], "я": [2, 3]}
    return dict_alfa

def get_list_dict(dict_alfa):
    new_list=[]
    for each_elem in dict_alfa:
        for count_letters in range(dict_alfa[each_elem][0]):
            new_list.append(each_elem)
    return new_list

def get_new_list_letters(user_word, user_list_letters):
    list_alfa = []
    for each_elem in user_list_letters:
        list_alfa.append(each_elem)
    for each_elem in user_word:
        if each_elem not in user_list_letters:
            return user_list_letters
        else:
            list_alfa.remove(each_elem)
    return list_alfa


def get_init_users(list_letters):
    user_letters = [[], []]
    user_letters[0], list_letters = get_new_letters(list_letters, 7)
    user_letters[1], list_letters = get_new_letters(list_letters, 7)

    print("Привет.\nМы начинаем играть в Scrabble")
    user_name = [input("Введите имя 1-го игрока: "), input("Введите имя 2-го игрока: ")]
    print(f"{user_name[0]} vs {user_name[1]}")
    print("-" * 20)
    print(f"Буквы игрока {user_name[0]}: {user_letters[0]}")
    print(f"Буквы игрока {user_name[1]}: {user_letters[1]}")
    return list_letters, user_name, user_letters

def get_score(word, dict_alffa):
    score=0
    for each_letter in word:
        score+=dict_alffa[each_letter][1]
    return score


def game():
    users_words = []
    total_score = [0, 0]
    list_words = get_words()

    dict_letters_base = get_dict_letters()
    list_letters_base=get_list_dict(dict_letters_base)
    list_letters, user_name, user_letters = get_init_users(list_letters_base)

    step = 0
    while len(list_letters) > 0 and (len(user_letters[0]) + len(user_letters[1])) > 0:
        numb_user = step % 2
        step += 1
        if not numb_user:
            print("- " * 15, "РАУНД", 1 + step // 2, " -" * 15)

        word = input(f"Ходит -{user_name[numb_user]}-. Придумайте слово, используя буквы: {user_letters[numb_user]}: ")
        word2 = word.replace("ё", "е")
        if word == "stop":
            break

        if word in list_words or word2 in list_words:  # есть ли слово в файле
            if word in users_words or word2 in users_words:  # было ли уже такое слово
                print(" " * 3, "Такое слово уже было! Попробуйте ещё раз")
                step -= 1
                continue
            else:  # такого слова еще не было
                new_list_letters = get_new_list_letters(word, user_letters[numb_user])
                if user_letters[numb_user] == new_list_letters:  # использовал не только свои буквы
                    new_alfa, list_letters = get_new_letters(list_letters, 1)
                    print(" " * 3, "Слово нужно составлять из своих букв!")
                else:  # использовал только свои буквы
                    new_alfa, list_letters = get_new_letters(list_letters, len(word) + 1)
                    print(" " * 3, "Есть такое слово!", end="")
                    users_words.append(word)
                    total_score[numb_user] += get_score(word, dict_letters_base)
                    print(f" Ваши очки увеличены на {get_score(word, dict_letters_base)}.")
                for each in new_alfa:
                    new_list_letters.append(each)
                user_letters[numb_user] = new_list_letters
        else:  # нет такого слова в файле
            new_alfa, list_letters = get_new_letters(list_letters, 1)
            print(" " * 3, "Такого слова нет!", end="")
            user_letters[numb_user].append(new_alfa[0])

        print(" " * 3, f"Вам добавлены буквы: {new_alfa}")
    return user_name, total_score


def print_statistik(users_name, totals_score):
    print("~" * 10)
    if totals_score[0] > totals_score[1]:
        print("Выигрывает", users_name[0])
    elif totals_score[0] < totals_score[1]:
        print("Выигрывает", users_name[1])
    else:
        print("У вас ничья!")
    print(f"Счет {totals_score[0]}:{totals_score[1]}")


if __name__ == "__main__":
    users_name, totals_score = game()
    print_statistik(users_name, totals_score)
