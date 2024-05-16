# Lowest Common Ancestor in a Binary Tree

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def findLCA(root,n1,n2):
    if root is None:
        return None
    if root.data==n1 and root.data==n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("LCA(4, 5) = ", findLCA(root, 4, 5).data)
print("LCA(4, 6) = ", findLCA(root, 4, 6).data)
