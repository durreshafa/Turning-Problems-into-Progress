class Solution:
    def check(self, nums: List[int]) -> bool:
        point = 0
        for i in range(1 , len(nums)):
            if nums[i-1] > nums[i]:
                point += 1

        if point == 0 or (point == 1 and nums[0] >= nums[-1]):
            return True
        return False
        