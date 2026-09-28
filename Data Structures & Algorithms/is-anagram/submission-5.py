class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT = {}
        countS = {}

        for c in s:
            countS[c] = countS.get(c, 0) + 1
        for c in t:
            countT[c] = countT.get(c, 0) + 1 

        return countT == countS
        