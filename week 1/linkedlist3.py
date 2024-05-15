#3 Search an element in a Linked List

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
    def search(self,li,key):
        if (not li):
            return False
        if li.data==key:
            return True
        return self.search(li.ref,key)

#Time Complexity: O(N)
#Auxiliary Space: O(N), Stack space used by recursive calls

li = Linkedlist()
li.push(10)
li.push(30)
li.push(21)
li.push(14)
li.printll()
x = 56
 # Function call
if li.search(li.head, x):
    print("\nYes")
else:
    print("\nNo")
