class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.items = []

    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Top from empty stack")
    
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)

        


        pass
    # You can implement this class however you like