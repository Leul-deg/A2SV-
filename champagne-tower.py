class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        rows = [[0] * i for i in range(1, query_row + 2)]
        rows[0][0] = poured


        valid = lambda i, nums: i >= 0 and i < len(nums)
        for i in range(1, len(rows)):
            for j in range(len(rows[i])):
                if valid(j - 1, rows[i - 1]):
                    if (rows[i - 1][j - 1] - 1) / 2 > 0:
                        rows[i][j] += ((rows[i - 1][j - 1] - 1) / 2)
                if valid(j, rows[i - 1]):
                    if (rows[i - 1][j] - 1) / 2 > 0:
                        rows[i][j] += ((rows[i - 1][j] - 1) / 2)
        # print(rows)
        return rows[query_row][query_glass] if rows[query_row][query_glass]  <= 1 else 1