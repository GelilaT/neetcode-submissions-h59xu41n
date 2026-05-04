class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        size = len(s1)
        l, r = 0, size - 1
        count = Counter(s1)
        while r < len(s2):
            cur = Counter(s2[l:r + 1])

            if count == cur:
                return True

            else:
                l += 1
                r += 1

        return False



        