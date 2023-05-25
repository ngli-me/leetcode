class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{' : '}',
                 '(' : ')',
                 '[' : ']'}
        if len(s) % 2 != 0:
            return False

        stack = []
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            elif len(stack) <= 0:
                return False
            elif pairs[stack.pop()] == char:
                continue
            else:
                return False
        # Return not stack is a smart way of checking the len
        return True if len(stack) == 0 else False



def main():
    s = Solution()
    input = "()[]{}"
    print(s.isValid(input));


if __name__ == "__main__":
    main()

