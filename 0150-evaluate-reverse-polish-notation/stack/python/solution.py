class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(num1, num2, operator):
            if operator == '+':
                return num1 + num2
            if operator == '-':
                return num1 - num2
            if operator == '*':
                return num1 * num2
            if operator == '/':
                return int(num1 / num2) # Truncate towards 0

        operand_stack = []
        for ele in tokens:
            if ele in {'+', '-', '*', '/'}:
                num2 = operand_stack.pop()
                num1 = operand_stack.pop()
                operand_stack.append(calculate(num1, num2, ele))
            else:
                operand_stack.append(int(ele))
        return operand_stack[0]
