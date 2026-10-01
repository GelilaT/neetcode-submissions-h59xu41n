class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mappings = {"2" : ["A", "B", "C"], 
        "3" : ["D", "E", "F"], 
        "4" : ["G", "H", "I"], 
        "5" : ["J", "K", "L"],
        "6" : ["M", "N", "O"], 
        "7" : ["P", "Q", "R", "S"], 
        "8" : ["T", "U", "V"], 
        "9" : ["W", "X", "Y", "Z"]}

        if not digits:
            return []

        n = len(digits)
        ans = []
        def backtrack(i, path):

            if len(path) == n:
                ans.append("".join(path))
                return 

            if i == n:
                return

            for val in mappings[digits[i]]:
                path.append(val)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return [word.lower() for word in ans]
        