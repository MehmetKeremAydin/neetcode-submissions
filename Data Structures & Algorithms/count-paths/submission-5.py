class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def recursiveBuild(m,n):
            if (m,n) in hashMap:
                return hashMap[(m,n)]
            if m == 1 or n == 1:
                return 1
            numPaths = recursiveBuild(m-1, n) + recursiveBuild(m, n-1)
            hashMap[(m,n)] = numPaths
            hashMap[(n,m)] = numPaths
            return numPaths
        hashMap = {}
        return recursiveBuild(m,n)
        