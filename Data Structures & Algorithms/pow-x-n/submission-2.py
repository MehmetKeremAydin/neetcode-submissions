class Solution:
    
    
    def myPow(self, x: float, n: int) -> float:
        def myPowR(x: float, n: int) -> float:
            if n == 1:
                return x
            half = self.myPow(x, n//2)
            return half * half if n%2 == 0 else half * half * x
        if n == 0:
            return 1
        signN = n / abs(n)
        n = abs(n)

        return myPowR(x, n) if signN == 1 else 1 / myPowR(x, n)
