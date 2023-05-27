from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search is O(logn)
        left = 0
        right = len(nums) - 1
        split = 0

        while left <= right:
            split = (left + right) // 2

            if nums[split] > target:
                right = split - 1
            elif nums[split] < target:
                left = split + 1
            else:
                return split
        # Not found
        return -1


def main():
    s = Solution()
    input = [5]
    print(s.search(input, -5));
    input2 = [-1,0,3,5,9,12]
    print(s.search(input2, -1))


if __name__ == "__main__":
    main()
