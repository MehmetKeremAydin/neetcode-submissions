class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            count = 0
            for bit in range(32):
                if i & (1 << bit):
                    count += 1
            answer.append(count)
        return answer


        
        