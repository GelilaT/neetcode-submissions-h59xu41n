class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        if len(s) == 1:
            return [1]

        partitions = []
        for left in range(len(s)):
            right = len(s) - 1
            while right >= left:
                if s[left] == s[right]:
                    partitions.append([left, right])
                    break

                right -= 1

        left = 0
        running_max = partitions[0][1]
        ans = []
        for right in range(1, len(partitions)):
            if partitions[right - 1][1] < partitions[right][0] and running_max < partitions[right][0]:
                ans.append(right - left)
                left = right         
            
            running_max = max(running_max, partitions[right][1])
        
        if left != len(partitions):
            ans.append(len(partitions) - left)

        return ans




