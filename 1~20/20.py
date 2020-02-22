class Solution:
    def isValid(self, s):
        if s == "":
            return True
        # Add a space to make it easier to judge the top element of the stack
        stack = [' ']
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c == ')':
                if stack.pop() != '(':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
            elif c == ']':
                if stack.pop() != '[':
                    return False
        
        return len(stack) == 1
