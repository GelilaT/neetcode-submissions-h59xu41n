class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = list(set(nums))
        parent = {i:i for i in nums}
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])

        def union(x, y):

            parentX = find(x)
            parentY = find(y)

            if parentX != parentY:
                parent[parentX] = parentY

        for num in nums:

            if num - 1 in parent:
                union(num - 1, num)

            if num + 1 in parent:
                union(num + 1, num)

        count = {}
        for num in nums:
            val = find(num)
            count[val] = count.get(val, 0) + 1

        return max(count.values()) if count else 0