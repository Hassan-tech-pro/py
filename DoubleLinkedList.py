class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 1. Basic Operations
    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def prepend(self, data):
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        else:
            node = Node(data)
            current = self.head
            for _ in range(index):
                current = current.next
            prev_node = current.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = current
            current.prev = node
            self.size += 1

    def remove_first(self):
        if not self.head:
            raise IndexError("List is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def remove_last(self):
        if not self.tail:
            raise IndexError("List is empty")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_first()
        elif index == self.size - 1:
            return self.remove_last()
        current = self.head
        for _ in range(index):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return current.data

    # 2. Access and Info
    def get_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set_at(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def contains(self, value):
        return self.index_of(value) != -1

    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def last_index_of(self, value):
        current = self.tail
        index = self.size - 1
        while current:
            if current.data == value:
                return index
            current = current.prev
            index -= 1
        return -1

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _len_(self):
        return self.size

    def _str_(self):
        return " <-> ".join(str(x) for x in self)

    def _iter_(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    # 3. Advanced Operations
    def reverse(self):
        current = self.head
        self.tail = current
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def clone(self):
        new_list = DoublyLinkedList()
        for data in self:
            new_list.append(data)
        return new_list

    def equals(self, other):
        if self.size != other.size:
            return False
        node1 = self.head
        node2 = other.head
        while node1 and node2:
            if node1.data != node2.data:
                return False
            node1 = node1.next
            node2 = node2.next
        return True

    def extend(self, other):
        for data in other:
            self.append(data)

    def to_list(self):
        return list(self)

    def from_list(self, lst):
        self.clear()
        for data in lst:
            self.append(data)

    def sort(self, reverse=False):
        self.from_list(sorted(self.to_list(), reverse=reverse))

    def rotate(self, k):
        if self.size == 0 or k % self.size == 0:
            return
        k %= self.size
        if k < 0:
            k += self.size

        split_point = self.size - k
        current = self.head
        for _ in range(split_point - 1):
            current = current.next

        new_head = current.next
        new_tail = current
        new_head.prev = None
        new_tail.next = None

        self.tail.next = self.head
        self.head.prev = self.tail

        self.head = new_head
        self.tail = new_tail

    def is_palindrome(self):
        front = self.head
        back = self.tail
        while front and back and front != back and front.prev != back:
            if front.data != back.data:
                return False
            front = front.next
            back = back.prev
        return True

    def swap(self, i, j):
        if i < 0 or j < 0 or i >= self.size or j >= self.size:
            raise IndexError("Index out of bounds")
        if i == j:
            return
        node1, node2 = None, None
        current = self.head
        for idx in range(max(i, j) + 1):
            if idx == i:
                node1 = current
            if idx == j:
                node2 = current
            current = current.next
        node1.data, node2.data = node2.data, node1.data

    def remove_duplicates(self):
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
            else:
                seen.add(current.data)
            current = current.next

    def split_at(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_list = DoublyLinkedList()
        if index == self.size:
            return new_list
        current = self.head
        for _ in range(index):
            current = current.next
        new_list.head = current
        new_list.tail = self.tail
        if current:
            current.prev.next = None
            current.prev = None
        self.tail = current.prev if current else self.tail
        self.size = index
        new_list.size = len(list(new_list))
        return new_list

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        return slow.data if slow else None

    def apply_function(self, func):
        current = self.head
        while current:
            current.data = func(current.data)
            current = current.next

    def filter(self, func):
        new_list = DoublyLinkedList()
        for data in self:
            if func(data):
                new_list.append(data)
        return new_list

    def map(self, func):
        new_list = DoublyLinkedList()
        for data in self:
            new_list.append(func(data))
        return new_list

    def reduce(self, func, initial):
        result = initial
        for data in self:
            result = func(result, data)
        return result

    def for_each(self, func):
        for data in self:
            func(data)

    def add_number(self, num):
        self.apply_function(lambda x: x + num)

    def multiply_number(self, num):
        self.apply_function(lambda x: x * num)

    def remove_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.remove_first()
                elif current == self.tail:
                    self.remove_last()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                return
            current = current.next
        raise ValueError("Value not found")

    def copy_to_array(self):
        return self.to_list()

    def reverse_iterator(self):
        current = self.tail
        while current:
            yield current.data
            current = current.prev