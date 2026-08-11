class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for t in tokens:

            if t in ["+", "-", "*", "/"]:
                popped1 = int(stack.pop())
                popped2 = int(stack.pop())

                if t == "+":
                    stack.append(popped1 + popped2)

                elif t == "-":
                    stack.append(popped2 - popped1)

                elif t == "*":
                    stack.append(popped1 * popped2)

                else:
                    stack.append(int(popped2 / popped1))

            else:
                stack.append(t)

        return int(stack[-1])
        