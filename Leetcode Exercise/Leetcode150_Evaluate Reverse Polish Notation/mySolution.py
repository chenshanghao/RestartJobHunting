class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmeticToken = {"+": 1, "-": 1, "*": 1, "/": 1}
        for token in tokens:
            if token in arithmeticToken:
                a, b = int(stack.pop()), int(stack.pop())
                res = 0
                if token == '+':
                    res = a + b
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(b / a)
                elif token == '-':
                    res = b - a
                stack.append(str(res))
            else:
                stack.append(token)
        return int(stack[0])
                    