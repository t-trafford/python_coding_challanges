class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def minDepth(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0

        # Base Case : Leaf node.This acoounts for height = 1
    ldepth = minDepth(root.left)
    rdepth = minDepth(root.right)

    if ldepth > rdepth:
        return ldepth +1
    else:
        return rdepth+1


# Driver Program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print (minDepth(root))
