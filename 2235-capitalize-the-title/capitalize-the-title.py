class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        arr = []
        for i in range (len(words)):
            if len(words[i]) <= 2:
                words[i] = words[i].lower()
            else:
                words[i] = words[i].lower()
                words[i] = words[i].capitalize()
            arr.append(words[i])
        ans = " ".join(arr)
        return ans
        