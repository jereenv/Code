class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {"+", "-", "/", "*"}
        for token in tokens:
            if token in operator:
                second = stack.pop()
                first = stack.pop()
                
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(int(token))
        return stack.pop()
        