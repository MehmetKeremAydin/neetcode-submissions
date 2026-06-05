class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        answer = []
        for num in count:
            if count[num] > len(nums) // 3:
                answer.append(num)

        return answer


        
        