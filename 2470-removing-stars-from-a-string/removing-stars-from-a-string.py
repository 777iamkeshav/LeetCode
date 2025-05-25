class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] # empty stack
        for char in s: # for every char in s
            if char == "*": # if char is equal to star
                if stack: # and if stack exists
                    stack.pop() # we pop from stack
            else: # if the char is not a "*"
                stack.append(char) # we append the char to stack
        return ''.join(stack) # returning the stack as output using .join function