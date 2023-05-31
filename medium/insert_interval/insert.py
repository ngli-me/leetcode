from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        j = 0
        for j, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                # No overlap
                result.append(interval)
            elif interval[0] > newInterval[1]:
                # new needs to be inserted before this one w/ no overlap
                result.append(newInterval)
                newInterval = interval
                break
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        result.append(newInterval)
        result += intervals[j+1:]

        return result

def main():
    s = Solution()
    print(s.insert([[1,5]], [2,3]))
    print(s.insert([[1,5]], [0,0]))
    print(s.insert([[1,5]], [2,7]))


if __name__ == "__main__":
    main()
