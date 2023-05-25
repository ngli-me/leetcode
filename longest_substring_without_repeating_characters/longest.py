class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = right = 0
        longest = 0

        while right < len(s):
            r = s[right]
            if r in chars:
                chars[r] += 1
            else:
                chars[r] = 1

            while chars[r] > 1:
                l = s[left]

                if l in chars:
                    chars[l] -= 1
                else:
                    chars[l] = -1

                left +=1

            longest = max(longest, right - left + 1)
            right += 1 
            print(left, right, chars)
        return longest

def main():
    s = Solution()
    input = "abcabcbb"
    print(s.lengthOfLongestSubstring(input));


if __name__ == "__main__":
    main()

