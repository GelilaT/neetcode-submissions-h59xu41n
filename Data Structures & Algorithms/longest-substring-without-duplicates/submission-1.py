class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1
        my_dict = {}
        l = r = 0

        while r < len(s):
            while s[r] in my_dict:
                del my_dict[s[l]]
                l += 1

            max_len = max(max_len, r - l + 1)
            my_dict[s[r]] = 1
            r += 1

        return max_len


        