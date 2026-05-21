class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
            
        elif n < 0:
            x = 1/x
            n += 1
        else:
            n -= 1
        
        multiplier = x
        while n != 0:
            x *= multiplier
            if n < 0:
                n += 1
            else:
                n -= 1

        return x
        