class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mappings = {2:["a", "b", "c"], 3:["d", "e", "f"], 4:["g", "h", "i"], 5:["j", "k", "l"], 6:["m", "n", "o"], 7:["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}

        ans = []
        def backtrack(i, path):

            if len(path) == len(digits) and len(digits) != 0:
                ans.append("".join(path))
                return 

            if i == len(digits):
                return 

            for val in mappings[int(digits[i])]:
                path.append(val)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return ans
        