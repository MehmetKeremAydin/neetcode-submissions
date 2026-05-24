class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recPerms(remNums:set, curPerm:list) -> None:
            #print(remNums, curPerm)
            if not remNums:
                answer.append(curPerm)
                return
            for entry in remNums:
                curPerm.append(entry)
                check = remNums.copy()
                check.remove(entry)
                recPerms(check, curPerm.copy())
                curPerm.pop()
            return
        
        answer = []
        perms = []
        nums = set(nums)
        recPerms(nums, perms)
        return answer