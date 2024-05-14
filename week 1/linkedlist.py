class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        if self.head is None:
            print("Ll is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'---->',end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def add_before(self,data,x):
        if self.head.data is None:
            print("LL is empty")
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("linkedlist is empty")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node





ll=Linkedlist()
ll.printlist()
ll.add_begin(10)
ll.add_before(20,10)
ll.add_after(30,10)
ll.add_end(9)
ll.printlist()
