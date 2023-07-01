import types


def flat_generator(list_of_lists):
    while list_of_lists:  # Пока список списков не пуст
        for elem in list_of_lists[0]:  # Перебираем элементы списка с индексом 0
            yield elem
        list_of_lists = list_of_lists[1::]  # Удаляем список с индексом 0 из списка списков


# Либо такая реализация функции flat_generator

# def flat_generator(list_of_lists):
#     list_of_lists = list_of_lists[::-1] # Разворачиваем список, чтобы в дальнейшем использовать pop
#     while list_of_lists:  # Пока список списков не пуст
#         for elem in list_of_lists.pop():  # Перебираем элементы списка с индексом -1 одновременно удаляя этот список из списка списков
#             yield elem


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
