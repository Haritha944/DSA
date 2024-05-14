# Tree
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)




tree=Tree()
root=tree.createNode(5)
print(root.data)
tree.insert(root,2)
tree.insert(root,4)
tree.insert(root,8)
tree.insert(root,16)
tree.insert(root,9)
print('Inorder------')
tree.traverse_inorder(root)
