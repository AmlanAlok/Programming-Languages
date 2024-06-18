from collections import deque

def ans(s):
    
    stack = deque()
    
    for c in s:
        
        if stack:
            if (stack[-1] == '(' and c == ')') or (stack[-1] == '{' and c == '}') or (stack[-1] == '[' and c == ']'):
                
                stack.pop()
                continue
                
        stack.append(c)
    
    return len(stack) == 0
