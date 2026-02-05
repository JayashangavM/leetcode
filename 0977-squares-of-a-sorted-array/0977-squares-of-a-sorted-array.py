class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            result.append(nums[i] * nums[i])
        
        result.sort()
        return result
