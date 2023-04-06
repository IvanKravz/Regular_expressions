import re
import csv

PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
SUB = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def name_correct(contact_list):
    new_list = []
    for data in contact_list:
        full_name = ' '.join(data[0:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], data[3], data[4],
                  re.sub(PATTERN, SUB, data[5]),
                  data[6]]
        new_list.append(result)

    return join_name(new_list)

# Функция создания список без одинаковых имен и фамилий, заполняя пустые значения name[] на new_name[]
def join_name(employees):
    for name in employees:
        first_name = name[0]
        last_name = name[1]
        for new_name in employees:
            new_first_name = new_name[0]
            new_last_name = new_name[1]
            if first_name == new_first_name and last_name == new_last_name:
                for i in range(2, 7):
                    if name[i] == "":
                        name[i] = new_name[i]
    result_list = []
    for employ in employees:
        if employ not in result_list:
            result_list.append(employ)

    return result_list

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(name_correct(contacts_list))

