#6 Delete the node from any position


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printll(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'--->',end=" ")
                n=n.ref
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def delete(self,data):
        if self.head is None:
            print("Linkedlist is empty")
        if data==self.head.data:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if data==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref

LL=Linkedlist()
LL.push(80)
LL.push(20)
LL.push(30)
LL.printll()
LL.delete(20)
print("\n After deletion")
LL.printll()
