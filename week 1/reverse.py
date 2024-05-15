# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,'--->',end=" ")
                n=n.ref
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def reverse(self):
        prev=None
        current=self.head
        while (current is not None):
            ref=current.ref
            current.ref=prev
            prev=current
            current=ref
        self.head = prev



# Driver code
llist = Linkedlist()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given linked list")
llist.printlist()
llist.reverse()
print ("\nReversed linked list")
llist.printlist()
