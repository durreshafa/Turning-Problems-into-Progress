class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = -1  

        for k in range(l, r + 1):  
            curr_sum = sum(nums[:k])  
            if curr_sum > 0:
                result = curr_sum if result == -1 else min(result, curr_sum)

            for i in range(k, len(nums)):
                curr_sum += nums[i] - nums[i - k] 
                if curr_sum > 0:
                    result = curr_sum if result == -1 else min(result, curr_sum)

        return result