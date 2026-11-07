class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1
        
        win = len(s1)
        win_count = {}
        for i in range(win):
            win_count[s2[i]] = win_count.get(s2[i], 0) + 1
        
        if win_count == count:
            return True 

        l = 0 
        for r in range(win, len(s2)):
            left = s2[l]
            win_count[left] -= 1
            if win_count[left] == 0:
                del win_count[left]
            l += 1

            win_count[s2[r]] = win_count.get(s2[r], 0) + 1
            if count == win_count:
                return True 
        return False