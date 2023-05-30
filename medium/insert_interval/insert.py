from typing import List

# This solution is maybe technically faster? O(logn) but aids to implement and runs better on larger sets
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # binary search to find which interval? then remove collisions
        left_start = 0
        right_start = len(intervals) - 1
        split_start = 0
        target_start = newInterval[0]
        while left_start <= right_start:
            # binary search against the last # in each interval
            split_start = (left_start + right_start) // 2
            if intervals[split_start][len(intervals[split_start]) - 1] > target_start:
                right_start = split_start - 1
            elif intervals[split_start][len(intervals[split_start]) - 1] < target_start:
                left_start = split_start + 1
            else:
                break

        left_end = 0
        right_end = len(intervals) - 1
        split_end = 0
        target_end = newInterval[len(newInterval) - 1]
        while left_end <= right_end:
            split_end = (left_end + right_end) // 2
            if intervals[split_end][0] > target_end:
                right_end = split_end - 1
            elif intervals[split_end][0] < target_end:
                left_end = split_end + 1
            else:
                break

        found_start = False
        start = []
        for i, inter in enumerate(intervals[split_start:split_end]):
            sub_index = 0
            while sub_index < len(inter):
                if inter[sub_index] >= target_start and inter[sub_index] <= target_end:
                    # this area will start overlap so save it
                    start = [i + split_start, sub_index]
                    found_start = True
                sub_index += 1
            if found_start:
                break
        print("start", start)

        backwards_index = split_end
        found_end = False
        end = []
        while backwards_index >= split_start:
            sub_index = len(intervals[backwards_index]) - 1
            while sub_index >= 0:
                if intervals[backwards_index][sub_index] <= target_end and \
                        intervals[backwards_index][sub_index] >= target_start:
                    # found interval area
                    end = [backwards_index, sub_index]
                    found_end = True
                sub_index -= 1
            backwards_index -= 1
            if found_end:
                break
        print("end", end)

        start_slice = split_start
        end_slice = split_end
        if found_start:
            # found overlap for the start position
            start_slice = start[0]
        if found_end:
            # found end
            end_slice = end[0]
        if not found_start and not found_end:
            # no overlap so just insert
            intervals.insert(split_start, newInterval)
            return intervals


        if end[1] == len(intervals[end[0]) - 1:
            # if remove the entire end interval
            end +=1
        if start[1] == 0:
            
        remove = end[0]
        remove_i = start[1]
            


        return(intervals)
        

def main():
    s = Solution()
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

    print(s.insert([[1,3],[6,9]], [2,5]))

if __name__ == "__main__":
    main()
