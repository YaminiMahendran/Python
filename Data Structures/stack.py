class Stack():
    
    def __init__(self):
        self.top = -1
        self.arr = []
        
    def printTop(self):
        print(self.top)
    
    def push(self, x):
        self.top += 1
        self.printTop()
        self.arr.insert(self.top, x)

    def pop(self):
        if self.isEmpty() != True:
            popped = self.arr[self.top]
            self.top -= 1
            return popped
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False