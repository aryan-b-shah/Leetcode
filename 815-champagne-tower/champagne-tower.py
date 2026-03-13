class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 102 for _ in range(102)]
        dp[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                if dp[r][c] > 1:
                    leftover = (dp[r][c] - 1.0) / 2.0
                    dp[r][c] = 1
                    dp[r + 1][c] += leftover
                    dp[r + 1][c + 1] += leftover
            
        return dp[query_row][query_glass]