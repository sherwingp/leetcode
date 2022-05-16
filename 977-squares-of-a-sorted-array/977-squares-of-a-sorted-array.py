class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            leftSquare = nums[l]**2
            rightSquare = nums[r]**2
            
            if leftSquare > rightSquare:
                result.insert(0, leftSquare)
                l += 1
            else:
                result.insert(0, rightSquare)
                r -= 1
        
        return result