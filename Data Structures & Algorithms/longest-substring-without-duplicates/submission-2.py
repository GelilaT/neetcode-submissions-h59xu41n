class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in count:
                count[s[left]] -= 1
                if not count[s[left]]:
                    del count[s[left]]
                
                left += 1

            count[s[right]] = 1
            max_len = max(max_len, right - left + 1)

        return max_len



        