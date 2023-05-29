from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Ig approach is, start at starting point, use map to hold checked locations, check directions
        # Prob should measure dict performance compared to checking the index
        # 4 initial checks, then maybe 3 if I configure it right?
        # Basically breadth first search

        dirs = [[0,1],
                [1,0],
                [0,-1],
                [-1,0]]

        checked = [[sr,sc]]
        queue = [[sr,sc]]
        initial_val = image[sr][sc]

        def check(direction: List[int]) -> bool:
            return (image[direction[0]][direction[1]] == initial_val)
            (0 <= direction[0] and direction[0] < len(image)) and \
            (0 <= direction[1] and direction[1] < len(image[1])) and \


        while queue:
            pt = queue.pop()
            image[pt[0]][pt[1]] = color

            vals = []
            for d in dirs:
                vals.append([d[0] + pt[0], d[1] + pt[1]])

            for v in vals:
                if v not in checked and check(v):
                    queue.append(v)
                checked.append(v)

        return image

def main():
    s = Solution()
    input = [[1,1,1],[1,1,0],[1,0,1]]
    print(s.floodFill(input, 1, 1, 2));


if __name__ == "__main__":
    main()

