class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0, 0
        count = [0] * 26
        max_len = 0

        while right < len(s):
            val = ord(s[right]) - ord('A')
            count[val] += 1
            while left < len(s) and (right - left + 1) - max(count) > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len



        