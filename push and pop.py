class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,data):
        self.stack.append(data)
        print self.stack
    def pop(self):
        if len(self.stack)<=0:
            return ("Stack Empty!")
        return self.stack.pop()
pp = Stack()
pp.push(10)
pp.push(20)
pp.push(30)
#pp.push('a')
print(pp.pop())
print(pp.pop())
print(pp.pop())
print(pp.pop())   
print(pp.pop())
