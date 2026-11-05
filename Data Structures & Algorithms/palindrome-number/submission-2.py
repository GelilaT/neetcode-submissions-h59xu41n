class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False

        if x < 9:
            return True

        num = ""
        temp = x
        while x > 0:
            val = x % 10
            num += str(val)
            x //= 10

        return int(num) == temp