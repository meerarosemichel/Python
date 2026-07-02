class Stack:
    def __init__(self):
        self.stack = []

    # Push 
    def push(self, value):
        self.stack.append(value)

    # Pop 
    def pop(self):
        if self.is_empty():
            return "Stack underflow"
        return self.stack.pop()

    # Peek 
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Check if empty
    def is_empty(self):
        return len(self.stack) == 0

    # Size 
    def size(self):
        return len(self.stack)

    # Search 
    def search(self, value):
        return value in self.stack

    # Display 
    def display(self):
        print(self.stack)


# Example 
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(100)
s.display()  
print(s.pop())  
s.display() 
print(s.peek())  