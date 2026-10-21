class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(t)
        if t == "":
            return ""

        count = {}
        cur = {}
        for i in range(n):
            count[t[i]] = count.get(t[i], 0) + 1

        left, right = 0, 0
        have = 0
        ans = ""
        min_len = math.inf
        need = len(count)
        while right < len(s): 
            cur[s[right]] = cur.get(s[right], 0) + 1
            if s[right] in count and cur[s[right]] == count[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]
                
                cur[s[left]] -= 1
                if s[left] in count and cur[s[left]] < count[s[left]]:
                    have -= 1
                
                left += 1

            right += 1

        return ans