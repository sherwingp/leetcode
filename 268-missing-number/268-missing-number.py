class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] < n and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i in range(n):
            if i != nums[i]:
                return i
        return n