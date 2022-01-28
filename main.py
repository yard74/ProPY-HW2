import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
def get_right_names(phonebook):
    new_phonebook = []
    i = 0
    for element in phonebook:
        if i == 0:
            new_phonebook.append(element)
            i += 1
        else:
            sep_name1 = element[0].split()
            if len(sep_name1) == 3:
                element[0] = sep_name1[0]
                element[1] = sep_name1[1]
                element[2] = sep_name1[2]
            if len(sep_name1) == 2:
                element[0] = sep_name1[0]
                element[1] = sep_name1[1]
            else:
                sep_name2 = element[1].split()
                if len(sep_name2) == 2:
                    element[1] = sep_name2[0]
                    element[2] = sep_name2[1]
            new_phonebook.append(element)
    return new_phonebook


def get_right_phones(phonebook):
    phone_pat1 = r"(\+7|8)(\s)?(\()?(\d{3})(\))?(\s)?(\-)?(\d{3})?(\-)?(\d{2})?"
    phone_pat2 = r"(\-)?(\d{2})?(\s)?(\()?([а-я.]{4})?(\s)?(\d{4})?(\))?"
    phone_pattern = phone_pat1 + phone_pat2
    phone_rep = r"+7(\4)\8-\10-\12\13\15\17"
    i = 0
    for element in phonebook:
        if i == 0:
            i += 1
            continue
        else:
            element[5] = re.sub(phone_pattern, phone_rep, element[5])
    return phonebook


def del_duplicates(phonebook):
    names_list = []
    names_dict = {}
    new_phonebook = []
    i = 0
    for element in phonebook:
        if i == 0:
            names_list.append((element[0], element[1]))
            names_dict[(element[0], element[1])] = element
            i += 1
        else:
            if (element[0], element[1]) not in names_list:
                names_list.append((element[0], element[1]))
                names_dict[(element[0], element[1])] = element
            else:
                name_value = names_dict[(element[0], element[1])]
                for n in range(7):
                    if name_value[n] == '':
                        name_value[n] = element[n]
                    else:
                        continue
                new_name_value = {(element[0], element[1]): name_value}
                names_dict.update(new_name_value)
    for value in names_dict.values():
        new_phonebook.append(value)
    return new_phonebook


right_names = get_right_names(contacts_list)
# print(right_names)
right_phones = get_right_phones(right_names)
# print(right_phones)
right_phonebook = del_duplicates(right_phones)
# print(right_phonebook)


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(right_phonebook)
