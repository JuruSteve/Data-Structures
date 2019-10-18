import sys
sys.path.append('../queue_and_stack')
from dll_stack import Stack
from dll_queue import Queue

# insert adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
# contains searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
# get_max returns the maximum value in the binary search tree.
# for_each performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # check if new node's val value < curr node val self.value
    # check if not self.left , self.left = BinarySearchTree(value)

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)

    # check if new node's val value < curr node val self.value
    # check if not self.left , self.left = BinarySearchTree(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        new_queue = Queue()
        new_queue.enqueue(node)
        while new_queue.len() > 0:
            current = new_queue.dequeue()
            print(current.value)
            if current.left:
                new_queue.enqueue(current.left)
            if current.right:
                new_queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        new_stack = Stack()
        new_stack.push(node)
        while new_stack.len() > 0:
            current = new_stack.pop()
            print(current.value)
            if current.left:
                new_stack.push(current.left)
            if current.right:
                new_stack.push(current.right)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# Testing
bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)