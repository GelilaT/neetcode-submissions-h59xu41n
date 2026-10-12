class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        root = TrieNode()
        ans = ""
        def insert(word):

            cur = root
            for idx, c in enumerate(word):
                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]
            
            cur.isEnd = True

        for word in strs:
            insert(word)

        cur = root
        while len(cur.children) == 1 and cur.isEnd == False:
            for key in cur.children.keys():
                cur = cur.children[key]
                ans += key

        return ans
                