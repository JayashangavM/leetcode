class Solution:
    def triangleType(self, nums: List[int]) -> str:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] + nums[j] <= nums[k] or nums[i] + nums[k] <= nums[j] or nums[j] + nums[k] <= nums[i]:
                        return "none"

                    if nums[i] == nums[j] == nums[k]:
                        return "equilateral"
                    elif nums[i] == nums[j] or nums[j] == nums[k] or nums[i] == nums[k]:
                        return "isosceles"
                    else:
                        return "scalene"
