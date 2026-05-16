class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2" : ["A", "B", "C"], 
        "3" : ["D", "E", "F"], 
        "4" : ["G", "H", "I"], 
        "5" : ["J", "K", "L"],
        "6" : ["M", "N", "O"], 
        "7" : ["P", "Q", "R", "S"], 
        "8" : ["T", "U", "V"], 
        "9" : ["W", "X", "Y", "Z"]}
        
        n = len(digits)
        ans = []
        def dfs(i, path):
            
            if len(path) == n and n != 0:
                ans.append("".join(path))
                return

            if i == n:
                return

            for val in my_dict[digits[i]]:
                path.append(val)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return [word.lower() for word in ans]

            

        