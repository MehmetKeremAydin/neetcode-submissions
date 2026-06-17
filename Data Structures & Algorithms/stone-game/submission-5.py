class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def recursiveSearch(left:int, right:int, turn:bool) -> int:
            if (left, right) in memory: return memory[(left, right)]
            if right < left:
                return 0
            count1 = recursiveSearch(left+1, right, not turn)
            count2 = recursiveSearch(left, right-1, not turn)
            if turn:
                count1 += piles[left]
                count2 += piles[right]
            memory[(left, right)] = max(count1, count2)
            return max(count1, count2)

        memory = {}
        total = sum(piles)
        aliceCount = recursiveSearch(0, len(piles)-1, True)
        return True if aliceCount > total // 2 else False