#Ex:1 
#Stacks and Queues
#stack and Queues
from collections import deque

def is_palindrome(input_str):
    # Normalize the input (optional: remove spaces, make lowercase)
    input_str = ''.join(input_str.lower().split())

    stack = [] # Stack: LIFO
    queue = deque() # Queue: FIFO

    # Fill stack and queue with characters
    for char in input_str:
        stack.append(char)
        queue.append(char)

    # Compare elements popped from stack and dequeued from queue
    while stack:
        if stack.pop() != queue.popleft():
            return False
    return True

# Test cases
print(is_palindrome("mom")) # Output: True
print(is_palindrome("Neveroddoreven")) # Output: True
print(is_palindrome("hello")) # Output: False

#stack
def is_balanced(expression):
    stack = [] # Stack to track opening parentheses
    matching_bracket = {')': '(', '}': '{', ']': '['} # Matching pairs

    for char in expression:
        if char in "({[":
            stack.append(char) # Push opening bracket to the stack
        elif char in ")}]":
            if not stack or stack.pop() != matching_bracket[char]:
                return False # Mismatch or unmatched closing bracket

    # If the stack is empty, all parentheses were matched
    return len(stack) == 0

# Test cases
print(is_balanced("(1+2)-3*[41+6]")) # Output: True
print(is_balanced("(1+2)-3*[41+6)")) # Output: False
print(is_balanced("(1+2)-3*[41+6")) # Output: False
print(is_balanced("(1+2)-3*]41+6[")) # Output: False
print(is_balanced("(1+[2-3]-4[41+6])")) # Output: True
