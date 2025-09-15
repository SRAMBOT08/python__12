def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():  # opening brackets
            stack.append(char)
        elif char in pairs:         # closing brackets
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# Example usage:
expr = "{[()]}()"
print(is_balanced(expr))  # True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

def is_balanced(s):
    stack = LinkedListStack()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

# Example usage:
expr = "{[()]}()"
print(is_balanced(expr))  # True

expr = "{[(])}"
print(is_balanced(expr))  # False
