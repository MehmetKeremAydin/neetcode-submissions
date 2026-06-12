class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recBT(curPerm, remNums):
            if len(curPerm) == len(nums):
                answer.add(tuple(curPerm))
                return
            for i in range(len(remNums)):
                curNum = remNums[i]
                curPerm.append(curNum)
                remNums.remove(curNum)
                recBT(curPerm.copy(), remNums.copy())
                curPerm.pop()
                remNums.insert(i, curNum)

        answer = set()
        curPerm = []

        recBT(curPerm, nums.copy())
        return list(answer)