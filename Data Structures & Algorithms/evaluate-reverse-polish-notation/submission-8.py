class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            try:
                stack.append(int(tokens[i]))
            except ValueError:
                a=stack.pop()
                b=stack.pop()
                if tokens[i] == "+":
                    stack.append(a+b)
                elif tokens[i] == "-":
                    stack.append(b-a)
                elif tokens[i] == "*":
                    stack.append(a*b)
                elif tokens[i] == "/":
                    stack.append(int(b/a))
        
        a = stack.pop()
        return a


        