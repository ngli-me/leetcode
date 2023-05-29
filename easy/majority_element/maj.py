def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            if n not in count.keys():
                count[n] = 1
            else:
                count[n] += 1

        return max(count, key=count.get)
