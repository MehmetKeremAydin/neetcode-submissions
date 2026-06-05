class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [False] * 3
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                check[0] = True
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                check[1] = True
            if triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]:
                check[2] = True
            if check[0] and check[1] and check[2]:
                return True
        return False
        