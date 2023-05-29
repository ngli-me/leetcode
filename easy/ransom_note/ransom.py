class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = {}

        for l in magazine:
            if l not in ransom_letters.keys():
                ransom_letters[l] = 1
            else:
                ransom_letters[l] += 1
        
        for l in ransomNote:
            if l not in ransom_letters.keys():
                return False
            else:
                ransom_letters[l] -= 1
                if ransom_letters[l] < 0:
                    return False
        return True
