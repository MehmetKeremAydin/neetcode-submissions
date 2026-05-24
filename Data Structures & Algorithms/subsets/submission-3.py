class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(2**len(nums)):
            availability = bin(i).split("b")[1]
            print(availability)
            subset = []
            for i,char in enumerate(reversed(availability)):
                if char == "1":
                    subset.append(nums[i])
            answer.append(subset)
        return answer