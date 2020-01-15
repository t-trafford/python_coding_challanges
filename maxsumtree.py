class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def total(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0

    if root.data < 0:
        root.data = 0

    return total(root.left) + total(root.right) + root.data


# Driver Program
root = Node(1)
root.left = Node(2)
root.right = Node(-3)
root.left.left = Node(4)
root.left.right = Node(5)
print (total(root))
