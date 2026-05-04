class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        size = len(s1)
        l = r = 0
        s1_dict = {}
        s2_dict = {}
        while r < size:
            s1_dict[s1[r]] = s1_dict.get(s1[r], 0) + 1
            s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1
            r += 1

        if s1_dict == s2_dict:
            return True

        while r < len(s2):
            
            s2_dict[s2[r]] = s2_dict.get(s2[r], 0) + 1
            s2_dict[s2[l]] = s2_dict[s2[l]] - 1
            if s2_dict[s2[l]] == 0:
                del s2_dict[s2[l]]
                
            if s1_dict == s2_dict:
                return True

            else:
                l += 1
                r += 1

        return False



        