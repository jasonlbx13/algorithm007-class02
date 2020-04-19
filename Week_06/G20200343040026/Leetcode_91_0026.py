# 动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0 or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s) + 1):

            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if i > 1 and 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]