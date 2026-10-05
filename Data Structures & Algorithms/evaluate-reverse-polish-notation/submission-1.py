class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+', '-', '*', '/'}

        for value in tokens:
            if value in operands:
                second_value = int(stack.pop())
                first_value = int(stack.pop())
                stack.append(str(self.Operation(first_value, second_value, value)))
                continue
            stack.append(value)
        
        return int(stack[-1])
            
            
    def Operation(self, first_value:int, second_value:int, operand:str) -> int:
        if operand == '+':
            return first_value + second_value
        elif operand == '-':
            return first_value - second_value
        elif operand == '*':
            return first_value * second_value
        elif operand == '/':
            return int(first_value / second_value)
