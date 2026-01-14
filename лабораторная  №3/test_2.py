# TODO Напишите функцию find_common_participants

def find_common_participants(group_1, group_2, sep = ','):
    answer = []
    _list1 = set(group_1.split(sep))
    _list2 = set(group_2.split(sep))
    answer.extend(_list1.intersection(_list2))
    answer.sort()
    return answer

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print(result)
# TODO Провеьте работу функции с разделителем отличным от запятой
