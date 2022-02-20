from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Node {value}'.format(
            value=str(self.value)
        )


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'{values}'.format(values=' '.join(values)).replace('\'', '').replace(',', ' ')
        return ''

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index: int) -> None:
        current_node = self.head
        current_index = 0
        previous = self.head
        if self.length == 0 or self.length < index:
            raise IndexError
        if current_node is not None:
            if index == 0:
                self.head = current_node.next
                self.length -= 1
                return
        while current_node is not None:
            if current_index == index:
                break
            previous = current_node
            current_node = current_node.next
            current_index += 1
        previous.next = current_node.next
        self.length -= 1

    def get(self, element: int) -> int:
        current_node = self.head
        index = 0
        if self.length == 0 or self.length < element:
            raise IndexError
        while current_node is not None:
            if element == index:
                return current_node.value
            current_node = current_node.next
            index += 1


snake = LinkedList()
snake.append(10)
snake.append(20)
snake.append(30)
snake.append('cat')
print('Текущий список:', snake)
print('Получение элемента:', snake.get(2))
print('Новый список:', snake)
print('Удаление элемента.')
snake.remove(3)
print('Новый список:', snake)
