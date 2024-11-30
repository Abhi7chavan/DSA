class Stack:
    def __init__(self):
        self.stack = []
        self.size = len(self.stack)
        
    def Push(self,element):
        return self.stack.append(element)
    
    def Pop(self):
        return self.stack.pop(-1)
    
    def Size(self):
        return len(self.stack)
    
    def Empty(self):
        return self.size < 1
    
    def Top(self):
        return self.stack[-1]
    
    
    
    
    
    
    
    
    