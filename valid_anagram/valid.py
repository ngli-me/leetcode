
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        return self.getMap(s) == self.getMap(t)

    def getMap(self, s: str) -> dict:
        di = {}
        for char in s:
            if char in di.keys():
                di[char]+=1
            else:
                di[char] = 1

        return di
def main():
    s = Solution()
    input1 = "anagram"
    input2 = "nagaram"
    print(s.isAnagram(input1, input2));


if __name__ == "__main__":
    main()
