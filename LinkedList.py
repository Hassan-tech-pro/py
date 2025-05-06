
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def _init_(self):
        self.head = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # 2. Insert at end
    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    # 3. Insert at position
    def insert_at_position(self, pos, data):
        if pos < 0:
            return
        if pos == 0:
            self.insert_at_beginning(data)
            return
        curr = self.head
        for _ in range(pos - 1):
            if not curr:
                return
            curr = curr.next
        if not curr:
            return
        node = Node(data)
        node.next = curr.next
        curr.next = node

    # 4. Delete at beginning
    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    # 5. Delete at end
    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    # 6. Delete by value
    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    # 7. Search element
    def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

    # 8. Get length
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # 9. Display list
    def display(self):
        curr = self.head
        elems = []
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print("Linked List:", elems)

    # 10. Reverse list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # 11. Get middle node
    def get_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    # 12. Get Nth from end
    def get_nth_from_end(self, n):
        fast = slow = self.head
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data if slow else None

    # 13. Remove duplicates
    def remove_duplicates(self):
        curr = self.head
        seen = set()
        prev = None
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr = curr.next

    # 14. Sort list
    def sort(self):
        if not self.head or not self.head.next:
            return
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next
        lst.sort()
        self.head = None
        for data in lst:
            self.insert_at_end(data)

    # 15. Find max value
    def find_max(self):
        if not self.head:
            return None
        max_val = self.head.data
        curr = self.head
        while curr:
            max_val = max(max_val, curr.data)
            curr = curr.next
        return max_val

    # 16. Find min value
    def find_min(self):
        if not self.head:
            return None
        min_val = self.head.data
        curr = self.head
        while curr:
            min_val = min(min_val, curr.data)
            curr = curr.next
        return min_val

    # 17. Sum of all elements
    def sum(self):
        total = 0
        curr = self.head
        while curr:
            total += curr.data
            curr = curr.next
        return total

    # 18. Count occurrences of value
    def count_occurrences(self, value):
        count = 0
        curr = self.head
        while curr:
            if curr.data == value:
                count += 1
            curr = curr.next
        return count

    # 19. Check if empty
    def is_empty(self):
        return self.head is None

    # 20. Clear the list
    def clear(self):
        self.head = None

    # 21. Convert to list
    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    # 22. Create from list
    def from_list(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    # 23. Detect cycle
    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 24. Create cycle
    def create_cycle(self, pos):
        if pos < 0:
            return
        cycle_node = None
        curr = self.head
        index = 0
        tail = None
        while curr:
            if index == pos:
                cycle_node = curr
            tail = curr
            curr = curr.next
            index += 1
        if tail:
            tail.next = cycle_node

    # 25. Remove cycle
    def remove_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        while fast.next != slow:
            fast = fast.next
        fast.next = None

    # 26. Clone list
    def clone(self):
        clone_list = SinglyLinkedList()
        curr = self.head
        while curr:
            clone_list.insert_at_end(curr.data)
            curr = curr.next
        return clone_list

    # 27. Merge with another list
    def merge(self, other):
        new_list = self.clone()
        curr = other.head
        while curr:
            new_list.insert_at_end(curr.data)
            curr = curr.next
        return new_list

    # 28. Alternate merge
    def alternate_merge(self, other):
        p1 = self.head
        p2 = other.head
        dummy = Node(0)
        tail = dummy
        toggle = True
        while p1 and p2:
            if toggle:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            toggle = not toggle
            tail = tail.next
        tail.next = p1 if p1 else p2
        result = SinglyLinkedList()
        result.head = dummy.next
        return result

    # 29. Check palindrome
    def is_palindrome(self):
        values = self.to_list()
        return values == values[::-1]

    # 30. Pairwise swap
    def pairwise_swap(self):
        curr = self.head
        while curr and curr.next:
            curr.data, curr.next.data = curr.next.data, curr.data
            curr = curr.next.next

    # 31. Rotate right
    def rotate_right(self, k):
        if not self.head or k == 0:
            return
        length = self.length()
        k %= length
        if k == 0:
            return
        fast = slow = self.head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    # 32. Rotate left
    def rotate_left(self, k):
        if not self.head or k == 0:
            return
        length = self.length()
        k %= length
        if k == 0:
            return
        curr = self.head
        for _ in range(k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail = new_head
        while tail and tail.next:
            tail = tail.next
        if tail:
            tail.next = self.head
        self.head = new_head

    # 33. Delete by position
    def delete_at_position(self, pos):
        if pos < 0 or not self.head:
            return
        if pos == 0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(pos - 1):
            if not curr.next:
                return
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    # 34. Insert after value
    def insert_after_value(self, target, data):
        curr = self.head
        while curr:
            if curr.data == target:
                node = Node(data)
                node.next = curr.next
                curr.next = node
                return
            curr = curr.next

    # 35. Insert before value
    def insert_before_value(self, target, data):
        if not self.head:
            return
        if self.head.data == target:
            self.insert_at_beginning(data)
            return
        curr = self.head
        while curr.next and curr.next.data != target:
            curr = curr.next
        if curr.next:
            node = Node(data)
            node.next = curr.next
            curr.next = node

    # 36. Get last node
    def get_last_node(self):
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr.data if curr else None

    # 37. Get first node
    def get_first_node(self):
        return self.head.data if self.head else None

    # 38. Get all indexes of a value
    def get_all_indexes(self, value):
        indexes = []
        index = 0
        curr = self.head
        while curr:
            if curr.data == value:
                indexes.append(index)
            curr = curr.next
            index += 1
        return indexes

    # 39. Replace value
    def replace(self, old_val, new_val):
        curr = self.head
        while curr:
            if curr.data == old_val:
                curr.data = new_val
            curr = curr.next

    # 40. Multiply all elements
    def product(self):
        if not self.head:
            return 0
        result = 1
        curr = self.head
        while curr:
            result *= curr.data
            curr = curr.next
        return result

    # 41. Average of elements
    def average(self):
        total = self.sum()
        count = self.length()
        return total / count if count else 0

    # 42. Get all even elements
    def get_evens(self):
        return [x for x in self.to_list() if x % 2 == 0]

    # 43. Get all odd elements
    def get_odds(self):
        return [x for x in self.to_list() if x % 2 != 0]

    # 44. Square all elements
    def square_elements(self):
        curr = self.head
        while curr:
            curr.data = curr.data ** 2
            curr = curr.next

    # 45. Cube all elements
    def cube_elements(self):
        curr = self.head
        while curr:
            curr.data = curr.data ** 3
            curr = curr.next

    # 46. Count prime numbers
    def count_primes(self):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        return sum(1 for x in self.to_list() if is_prime(x))

    # 47. Filter by condition (lambda)
    def filter(self, func):
        filtered = SinglyLinkedList()
        curr = self.head
        while curr:
            if func(curr.data):
                filtered.insert_at_end(curr.data)
            curr = curr.next
        return filtered

    # 48. Map values (lambda)
    def map(self, func):
        curr = self.head
        while curr:
            curr.data = func(curr.data)
            curr = curr.next

    # 49. Reduce values (lambda)
    def reduce(self, func, initializer=None):
        from functools import reduce
        return reduce(func, self.to_list(), initializer) if initializer is not None else reduce(func, self.to_list())

    # 50. Zip with another list (like zip())
    def zip_with(self, other):
        result = []
        p1 = self.head
        p2 = other.head
        while p1 and p2:
            result.append((p1.data, p2.data))
            p1 = p1.next
            p2 = p2.next
        return result
