#ex 2
#stack
def decode_message(message):
    stack = [] # Initialize an empty stack

    # Loop through each character in the input message
    for char in message:
        if char == '*':
            if stack: # Pop the top character if the stack is not empty
                stack.pop()
        else:
            stack.append(char) # Push characters and spaces to the stack

    # Join the remaining characters from the stack to form the decoded message
    return ''.join(stack)

# Test the example from the problem
input_message = "SIVLE ****** DAED TNSI ***"
decoded_message = decode_message(input_message)
print(decoded_message) # Output: ELVIS ISNT DEAD