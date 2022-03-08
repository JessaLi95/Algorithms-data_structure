# Binary tree:
# Full tree (every parent has 2 nodes)
# Complete tree (fill the tree from left to right)
# Perfect tree (all parents on the level are filled)
# leaf: nodes don't have children


# Binary search tree: O(log n)
# Get a node and compare the value with existing nodes from the root
# Smaller goes left, bigger goes right

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1