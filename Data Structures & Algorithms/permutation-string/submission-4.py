class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count = {}
        count2 = {}
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        if count == count2:
            return True

        left, right = 0, len(s1)
        while right < len(s2):
            count2[s2[left]] -= 1
            count2[s2[right]] = count2.get(s2[right], 0) + 1
            if not count2[s2[left]]:
                del count2[s2[left]]

            if count2 == count:
                return True

            left += 1
            right += 1

        return False
            






        