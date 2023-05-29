class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for c in s:
            if c not in letters.keys():
                letters[c] = 1
            else:

                letters[c] += 1

        has_rando = False
        total_len = 0
        for c in letters.keys():
            if letters[c] >= 1:
                if letters[c] % 2 == 0:
                    total_len += letters[c]
                else: 
                    total_len += (letters[c] - 1)
                    has_rando = True
        
        return total_len + 1 if has_rando else total_len
