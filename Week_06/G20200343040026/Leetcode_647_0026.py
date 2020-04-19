# 动态规划
class Solution:
    def countSubstrings(self, s: str) -> int:
        if s=='':
            return 0
        cnt = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j,-1,-1):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    cnt += 1
        return cnt