"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node = self.head
        self.length += 1

    def remove_from_head(self):
        val = self.head.value
        self.delete(self.head)
        self.length -= 1
        return val

    def add_to_tail(self, value):
        new_node = ListNode(value, None, self.head)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node = self.tail
        self.length += 1

    def remove_from_tail(self):
        val = self.tail.value
        self.delete(self.tail)
        self.length -= 1
        return val

    def move_to_front(self, node):
        if node is self.head:
            return
        val = node.value
        self.delete(node)
        self.add_to_head(val)

    def move_to_end(self, node):
        if node is self.tail:
            return
        val = node.value
        self.delete(node)
        self.add_to_tail(val)

    def delete(self, node):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif not self.head:
            return None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            self.delete(node)

    def get_max(self):
        if not self.head:
            return None
        curr_max = 0
        current_val = self.head.value
        while current_val:
            if current_val > curr_max:
                curr_max = current_val
                current_val = current_val.next
        return curr_max


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.dict_storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.dict_storage:
            return None
        else:
            node = self.dict_storage[key]
            self.storage.move_to_end(node)
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key not in self.dict_storage:
            return None
        else:
            node = self.dict_storage[key]
            node.value = (key, value)
            self.storage.move_to_end(node)
            return

        if self.size == self.limit:
            del self.dict_storage[self.storage.remove_from_tail()[0]]
            self.size -= 1
        self.storage.add_to_tail((key, value))
        self.dict_storage[key] = self.storage.tail
        self.size -= 1
