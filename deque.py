# 81319040
from typing import Tuple


class QueueIsFull(Exception):
    pass


class QueueIsEmpty(Exception):
    pass


class MyQueueSized:
    def __init__(self, max_size):
        self.__max_size: int = max_size
        self.__queue: list = [None] * max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size_of_queue: int = 0

    def _is_empty(self) -> int:
        return self.__size_of_queue == 0

    def _queue_is_full(self) -> bool:
        return self.__size_of_queue >= self.__max_size

    def _get_index_by_method(self, name) -> int:
        results = {
            'push_front': self.__head - 1,
            'push_back': self.__tail + 1,
            'pop_front': self.__head + 1,
            'pop_back': self.__tail - 1
        }
        index = results.get(name) % self.__max_size
        return index

    def push_front(self, x) -> None:
        if self._queue_is_full():
            raise QueueIsFull

        self.__head = self._get_index_by_method(self.push_front.__name__)
        self.__queue[self.__head] = x
        self.__size_of_queue += 1

    def push_back(self, x) -> None:
        if self._queue_is_full():
            raise QueueIsFull

        self.__queue[self.__tail] = x
        self.__tail = self._get_index_by_method(self.push_back.__name__)
        self.__size_of_queue += 1

    def pop_front(self) -> int:
        if self._is_empty():
            raise QueueIsEmpty

        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self._get_index_by_method(self.pop_front.__name__)
        self.__size_of_queue -= 1
        return x

    def pop_back(self) -> int:
        if self._is_empty():
            raise QueueIsEmpty

        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = self._get_index_by_method(self.pop_back.__name__)
        self.__size_of_queue -= 1
        return x


def read_input() -> Tuple[int, int]:
    number_of_commands = int(input())
    max_size = int(input())
    return number_of_commands, max_size


def main() -> None:
    n, m = read_input()
    instance = MyQueueSized(m)
    for _ in range(n):
        method, *value = input().split()
        try:
            if value:
                getattr(instance, method)(int(*value))
            else:
                print(getattr(instance, method)())
        except (QueueIsEmpty, QueueIsFull):
            print('error')


if __name__ == '__main__':
    main()