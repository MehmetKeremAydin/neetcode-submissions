class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recSearch(i, curComb):
            if len(curComb) == k:
                answer.append(curComb)
                return
            if i > n:
                return
            recSearch(i+1, curComb.copy())
            curComb.append(i)
            recSearch(i+1, curComb.copy())
        

        
        answer = []
        curComb = []
        recSearch(1, curComb)
        return answer
        