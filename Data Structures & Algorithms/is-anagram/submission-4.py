class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countT = {}
        countS = {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        
        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
        
        return countT == countS

        