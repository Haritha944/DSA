#2 Write a function to count the number of nodes in a given singly linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'--->',end='')
                n=n.ref
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def getcount(self):
        temp=self.head
        count=0
        while (temp):
            count+=1
            temp=temp.ref
        return count

LL=Linkedlist()
LL.push(3)
LL.push(4)
LL.push(7)
LL.print_ll()
print("\nCount of nodes",LL.getcount())
