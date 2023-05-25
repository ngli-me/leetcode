import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while (s[left] in string.punctuation or s[left] == ' ') and left < right: left +=1
            while (s[right] in string.punctuation or s[right] == ' ') and left < right: right -=1
            print(left, right, s[left], s[right])
            if s[left].lower() != s[right].lower(): return False
            left +=1
            right -=1
        return True

def main():
    s = Solution()
    input = 'A man, a plan, a canal: Panama' 
    r = s.isPalindrome(input)
    print(r)

if __name__ == "__main__":
    main()

