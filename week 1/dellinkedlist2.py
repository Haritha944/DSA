#5 deletion of node at the end

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printll(self):
        if self.head is None:
            print('Linkedlist is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.ref
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def delete_end(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
           if self.head.ref is None:  # Check if there's only one node
                self.head = None  # Set head to None if it's the only node
           else:
                n = self.head
                while n.ref.ref is not None:  # Traverse until second last node
                    n = n.ref
                n.ref = None  # Set the next of second last node to None to delete the last node

LL=Linkedlist()
LL.push(10)
LL.push(20)
LL.push(30)
LL.printll()
LL.delete_end()
print("\n After deletion")
LL.printll()
