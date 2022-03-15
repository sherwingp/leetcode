class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        degree = max(freq.values())
        res_freq = {}
        
        left, window, min_window = 0, 0, math.inf
        
        for i in range(len(nums)):
            window += 1
            if nums[i] in res_freq:
                res_freq[nums[i]] += 1
            else:
                res_freq[nums[i]] = 1
            
            while max(res_freq.values()) == degree:
                min_window = min(min_window, window)
                res_freq[nums[left]] -= 1
                left += 1
                window -= 1
        return min_window
            