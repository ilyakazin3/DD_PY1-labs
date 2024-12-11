# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, sep=","):
    set2 = set(str1.split(sep))
    set1 = set(str2.split(sep))
    return sorted(set1 & set2)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
