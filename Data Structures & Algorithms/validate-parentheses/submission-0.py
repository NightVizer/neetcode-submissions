class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for value in s:
            if not stack:
                stack.append(value)
                continue
            
            if self.IsOpposite(stack[-1], value):
                stack.pop()
            else:
                stack.append(value)
        
        if stack:
            return False

        return True
    
    def IsOpposite(self, last_elemet: str, current_element: str) -> bool:
        if last_elemet == "[":
            if current_element == "]":
                return True
        if last_elemet == "{":
            if current_element == "}":
                return True
        if last_elemet == "(":
            if current_element == ")":
                return True
        return False