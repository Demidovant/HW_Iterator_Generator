class FlatIterator:

    def __init__(self, main_list):
        self.main_list = main_list

    def __iter__(self):
        self.list_of_iters = [iter(self.main_list)]
        return self

    def __next__(self):
        while self.list_of_iters:
            try:
                next_item = next(self.list_of_iters[-1])  # пытаемся получить следующий элемент, если не получилось, значит итератор пустой
            except StopIteration:
                self.list_of_iters.pop()
                continue

            if isinstance(next_item, list):
                # если следующий элемент оказался списком, то добавляем его итератор в list_of_iters
                self.list_of_iters.append(iter(next_item))

            else:
                return next_item
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
