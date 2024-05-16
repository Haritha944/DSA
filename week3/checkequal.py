#Program to Determine if given Two Trees are Identical or not

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
    def identical_trees(a,b):
        if a is None and b is None:
            return True
        if a is not None and b is not None:
            return ((a.key == b.key) and Node.identical_trees(a.left,b.left) and Node.identical_trees(a.right,b.right))
        return False
root1=Node(1)
root1.left=Node(2)
root1.right=Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2=Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
if Node.identical_trees(root1, root2):
    print("Both trees are identical")
else:
    print("Trees are not identical")
