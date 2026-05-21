class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        resLen = 0
        n = len(s)
        def inbound(l, r):
            return l >= 0 and r < n

        for i in range(n):

            l, r = i, i
            while inbound(l, r) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            l, r = i, i + 1
            while inbound(l, r) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

        return res


        