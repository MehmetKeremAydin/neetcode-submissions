class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        primeMemory = {1:set([]), 2:set([2]), 3:set([3])}
        def getPrimeDivisors(num:int, begin) -> set:
            if num in primeMemory:
                return primeMemory[num]
            print(int(num**0.5))
            for i in range(begin, int(num**0.5+1)):
                if num % i == 0:
                    while num % i == 0:
                        num //= i
                    divs = getPrimeDivisors(num, i+1)
                    divs.add(i)
                    return divs
            primeMemory[num] = set([num])
            return primeMemory[num]
        
        def find(i):
            while parents[i] != i:
                i = parents[i]
            return i
        
        def union(i,j):
            pi, pj = find(i), find(j)
            if pi == pj: return False
            if rank[pi] >= rank[pj]:
                rank[pi] += rank[pj]
                parents[pj] = pi
            else:
                rank[pj] += rank[pi]
                parents[pi] = pj
            return True

        rank = [1] * len(nums)
        parents = [i for i in range(len(nums))]
        connections = []
        for num in nums:
            connections.append(getPrimeDivisors(num, 2))
        print(connections)
        i = 0
        while max(rank) < len(nums) and i < len(nums):
            for j in range(i+1, len(nums)):
                allDivs = connections[i].union(connections[j])
                if len(allDivs) < len(connections[i]) + len(connections[j]):
                    union(i,j)
            i += 1
    
        return False if i == len(nums) else True
