#4 Deletion of node in linkedlist


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
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
            return
        else:
            self.head=self.head.ref


LL=Linkedlist()
LL.push(10)
LL.push(20)
LL.push(30)
LL.printll()
LL.delete_begin()
print("\n After deletion")
LL.printll()
