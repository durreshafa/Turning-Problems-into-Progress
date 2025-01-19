class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])
        
        # length = len(arr)
        # last = len(arr[length-1])
        # return last
        