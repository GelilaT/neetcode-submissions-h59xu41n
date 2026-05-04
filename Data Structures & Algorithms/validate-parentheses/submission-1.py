class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        my_dict = {")": "(", "}":"{", "]":"["}

        for i in range(len(s)):

            if s[i] in ("(", "{", "["):
                stack.append(s[i])
                continue

            if not stack or stack and stack[-1] != my_dict[s[i]]:
                return False

            if stack:   
                stack.pop()

        return True if not stack else False
        

        