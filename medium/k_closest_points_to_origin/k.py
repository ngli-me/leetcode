from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        for pt in points:
            d = round(math.sqrt(pt[0]**2 + pt[1]**2), 4)
            if d in distances.keys():
                distances[d].append(pt)
            else:
                distances[d] = [pt]
            # print(distances)

        keys = list(distances.keys())
        keys.sort()
        if k == 1:
            return distances[keys[0]]
        ret = []
        count = 0
        for i in range(0, k):
            if count == k:
                break
            print(i, k, keys)
            for pt in distances[keys[i]]:
                if count == k:
                    break
                ret.append(pt)
                count += 1
        return ret


def main():
    s = Solution()
    print(s.kClosest([[0,1],[1,0]], 2))
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))

    print(s.kClosest([[1,3],[-2,2]], 1))

if __name__ == "__main__":
    main()
