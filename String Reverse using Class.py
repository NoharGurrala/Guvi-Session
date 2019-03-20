global arr
arr = []
class Rev:
    def __init__(self):
        self.arr=arr
    def reve(self,arr):
        if len(arr) == 0:
            return arr
        else:
            return (reve.reve(arr[1:]) + (arr[0]))
reve = Rev()
arr = raw_input()
print(reve.reve(arr))

