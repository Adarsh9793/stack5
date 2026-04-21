# Stack implementation using linked list and "postfix expression evaluation" to infix conversion"
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")  # dummy head node
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def push(self, val):
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.val   # return value, not Node
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.head.next.val   # return value, not Node
    
def postfixToInfix(givenStr):
    ops = ['+', '-', '*', '/']
    mystack = Stack()
    for i in givenStr:
        if i in ops:
            second = mystack.pop()
            first = mystack.pop()
            mystack.push('(' + first + i + second + ')')

        else:
            mystack.push(i)

    return mystack.pop()   # return value

# Test
givenStr = ['2', '3', '1', '*', '+', '9', '-']
print(postfixToInfix(givenStr))  # '((2+(3*1))-9)'