class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextEl = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[nextEl] = nums[i]
                nextEl += 1
        return nextEl