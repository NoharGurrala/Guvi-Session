class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):

        if self.data:   #If data is present
            if data < self.data:    #if data is less
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:  #Is data is greater
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return "\n\n"+str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return "\n\n"+str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            return("\n"+str(self.data) + ' is found')



    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

            
head=input("Enter the head node:")
l = input("Enter the tree size:")
root = Node(head) #Head Node
for i in range(0,l):
    j = input("Enter the element to insert in tree:")
    root.insert(j)
root.PrintTree()
f = input("\n\nEnter the element to find in tree:")
print(root.findval(f))
