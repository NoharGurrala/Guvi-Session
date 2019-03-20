class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
    def add(self, newdata):
        NewNode = Node(newdata)
        if self.headval.dataval is None:
            self.headval = NewNode
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
        


    def printlist(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval),
            printval = printval.nextval


    def conti(self):
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=self.headval
        print ("It is continuious")

list = LinkedList()
n = input('Number of nodes : ')
h = input('Enter the head node : ')
list.headval = Node(h)
for i in range(0,n-1):
    list.add(input('Enter the Element : '))
list.printlist()
r = input('Do you want to make it continues :\n1 - YES\n0 - NO\n:')
if( r == 1):
    list.conti()
    list.printlist()
