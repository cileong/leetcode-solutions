class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        if neg:
            x = -x

        res = 0
        while x:
            res = res*10 + x%10
            x //= 10

        if not -2**31 <= res <= 2**31 - 1:
            return 0
        else:
            return -res if neg else res