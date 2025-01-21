class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        x,y,z = nums
        if x+y <= z or y+z <= x or z+x <= y:
            return "none"
        else:
            if x == y == z:
                return "equilateral"
            elif x == y or y == z or z == x :
                return "isosceles"
            else:
                return "scalene"