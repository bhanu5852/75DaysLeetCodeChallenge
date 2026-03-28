class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next
            window_sum -= nums[i-k]    # remove previous
            
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k