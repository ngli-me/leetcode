# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            split = (left + right) // 2
            if isBadVersion(split):
                right = split
            else:
                left = split + 1

        return left

def main():


if __name__ == "__main__":
    main()
