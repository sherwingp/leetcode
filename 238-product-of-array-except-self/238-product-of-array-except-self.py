class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        tmp = 1
        # left side
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        
        tmp = 1
        # right side
        for i in range(len(nums) -1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        
        return res