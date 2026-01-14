# TODO Напишите функцию для поиска индекса товара

def find_index(fi, list_):
    answer = None
    for i, value in enumerate(list_):
        if value == fi:
            answer = i
            break
    return answer
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(find_item, items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
