import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","/","*"}
        for token in tokens:
            if token in operations:
                second = stack.pop()
                first = stack.pop()
                
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    val = first / second
                    if val < 0:
                        val = math.ceil(val)
                    else:
                        val = math.floor(val)
                    stack.append(val)
            else:
                stack.append(int(token))
        
        return stack[-1]
                    
                
            
        