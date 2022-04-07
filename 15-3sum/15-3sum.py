class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = num + nums[l] + nums[r]
                
                if threesum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1
        return res