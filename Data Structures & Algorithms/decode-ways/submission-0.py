class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s) 

        dp = [0] * (n + 1)

        dp[0] = 1 

        for i in range(1, n + 1):
            #take 1 
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            if i >=2:
                first = s[i - 2]
                sec = s[i - 1]
                if first == "1" or (first == "2" and sec in ('0123456')):
                    dp[i] += dp[i - 2]
            
        
        return dp[n]


        
        