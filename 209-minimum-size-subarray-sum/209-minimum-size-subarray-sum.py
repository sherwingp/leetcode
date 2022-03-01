class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0 
        min_len = math.inf
        window_start = 0
        
        for window_end in range(0, len(nums)):
            window_sum += nums[window_end]
            
            while window_sum >= target:
                min_len = min(min_len, window_end - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
        
        if min_len == math.inf:
            return 0
        return min_len