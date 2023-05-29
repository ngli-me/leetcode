class Solution:
    def climbStairs(self, n: int) -> int:
        # 1,1 = 2
        # n = 1 is 1
        # n = 2 is 2
        # n = 3 3
        # n = 4 1,1,1,1 1,2,1 2,1,1 1,1,2 2,2  5 total
        # n = 5 {n=4} + 3 = 8
        # fibo

        prev = 1
        cur = 1
        tmp = 0

        for i in range(1,n):
            tmp = cur
            cur = cur + prev
            prev = tmp
        return cur
