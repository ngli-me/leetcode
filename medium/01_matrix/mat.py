from typing import List
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    mat[i][j] = min(mat[i - 1][j] if i > 0 else 10**4, \
                            mat[i][j - 1] if j > 0 else 10**4) + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] > 0:
                    mat[i][j] = min(mat[i][j], \
                            (mat[i + 1][j] if i < m - 1 else 10**4) + 1, \
                            (mat[i][j + 1] if j < n - 1 else 10**4) + 1)

        return mat


def main():
    s = Solution()
    print(s.updateMatrix([[0,0,0,1,1,1,1,1,1]]))


if __name__ == "__main__":
    main()
