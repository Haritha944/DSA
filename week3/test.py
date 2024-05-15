#Find the Maximum Depth or Height of given Binary Tree

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def maxDepth(self):
        if self is None:
            return 0
        else:
            lDepth = 0 if self.left is None else self.left.maxDepth()
            rDepth = 0 if self.right is None else self.right.maxDepth()
            return max(lDepth, rDepth) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left=Node(3)
root.left.right=Node(7)

print("Height of tree is %d" % (root.maxDepth()))
