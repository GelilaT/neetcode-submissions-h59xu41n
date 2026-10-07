class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n):

            total = 0
            while n >= 10:
                total += ((n % 10) ** 2)
                n //= 10

            total += (n ** 2)
            return total

        visited = set()
        while n not in visited:
            visited.add(n)
            n = helper(n)
            if n == 1:
                return True

        return False
        

        

        