class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        count = [0] * len(fruits)
        left, right, k = 0, 0, 0
        max_fruits = 0
        while right < len(fruits):
            if count[fruits[right]] == 0:
                k += 1

            count[fruits[right]] += 1
            while k > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    k -= 1

                left += 1

            max_fruits = max(max_fruits, sum(count))
            right += 1

        return max_fruits
            


            