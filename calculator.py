# 81348000
OPERATIONS = {
    '+': lambda x, y: y + x,
    '-': lambda x, y: y - x,
    '*': lambda x, y: y * x,
    '/': lambda x, y: y // x,
}


class Stack:
    
    def __init__(self) -> None:
        self.__items = []
    
    def push(self, item: int) -> None:
        self.__items.append(item)
    
    def pop(self) -> int:
        return self.__items.pop()


def read_input() -> list:
    chars: list = input().split()
    return chars


def calc(stack: Stack, list_of_symbols: list) -> list:
    for symbol in list_of_symbols:
        if symbol in OPERATIONS:
            operation = OPERATIONS[symbol]
            stack.push(operation(stack.pop(), stack.pop()))
        else:
            stack.push(int(symbol))
    return stack.pop()


def main() -> None:
    list_of_symbols = read_input()
    stack = Stack()
    result = calc(stack, list_of_symbols)
    print(result)


if __name__ == '__main__':
    main()