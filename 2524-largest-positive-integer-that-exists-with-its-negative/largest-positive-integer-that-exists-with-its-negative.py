class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            max_nums = max(nums)
            if -max_nums in nums:
                return max_nums
            else:
                nums.remove(max_nums)
        return -1



        # nums.sort()  
        # for num in reversed(nums):  
        #     if -num in nums:  
        #         return num  
        # return -1 