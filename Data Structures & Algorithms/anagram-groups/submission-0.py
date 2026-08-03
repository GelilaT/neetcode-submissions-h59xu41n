class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            my_dict[tuple(count)].append(word)

        return list(my_dict.values())

        