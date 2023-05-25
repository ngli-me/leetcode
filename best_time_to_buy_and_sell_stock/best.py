from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Looks like O(n)
        # Need to loop through once since not sorted
        # As you go, put the price in the stack, then find everything in the stack before and check
        # if the price is lower, save the max amount
        # Actually, dont need a stack just need the min

        profit = 0
        prev_min = 10 ** 5
        for day in prices:
            if day > prev_min:
                calc = day - prev_min
                profit = calc if calc > profit else profit
            else:
                prev_min = day
            print(day, prev_min, profit)
        
        return profit

def main():
    s = Solution()
    input = [7,1,5,3,6,4]
    r = s.maxProfit(input)
    print(r)
    # Holy crap says my solution beats 99.9% for runtime how lol

if __name__ == "__main__":
    main()

