#8.Given a singly linked list consisting of N nodes. The task is to remove
# duplicates (nodes with duplicate values) from the given list (if exists).


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'--->',end="")
                n=n.ref
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def removeduplicates(self):
        if self.head is None:
            print("Linekdlist is empty")
        seen_values=set()
        current=self.head
        prev=None
        while current is not None:
            if current.data in seen_values:
                prev.ref=current.ref

            else:
                seen_values.add(current.data)
                prev=current
            current=current.ref

ll=Linkedlist()
ll.push(10)
ll.push(20)
ll.push(40)
ll.push(10)
ll.printll()
print("\n")
ll.removeduplicates()
ll.printll()
