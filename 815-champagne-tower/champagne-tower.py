class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 2)
        dp[0] = float(poured)

        for row in range(query_row):
            for glass in range(row, -1, -1):
                overflow = max(0.0, (dp[glass] - 1.0) / 2.0)
                dp[glass] = overflow
                dp[glass + 1] += overflow

        return min(1.0, dp[query_glass])
        # dp = [[0] * 102 for _ in range(102)]
        # dp[0][0] = poured

        # for r in range(query_row + 1):
        #     for c in range(r + 1):
        #         if dp[r][c] > 1:
        #             leftover = (dp[r][c] - 1.0) / 2.0
        #             dp[r][c] = 1
        #             dp[r + 1][c] += leftover
        #             dp[r + 1][c + 1] += leftover
            
        # return dp[query_row][query_glass]