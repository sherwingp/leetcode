class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_num = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[next_num-1]:
                nums[next_num] = nums[i]
                next_num += 1
        return next_num