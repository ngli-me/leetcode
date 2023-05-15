class Solution {
public:
    int start_row = 0;
    int start_col = 0;
    int end_row;
    int end_col;


    std::vector<int> horizontal(vector<vector<int>>& matrix, int start, int end, int dir);

    std::vector<int> vertical(vector<vector<int>>& matrix, int start, int end, int dir);

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        end_row = matrix.size();
        end_col = matrix[0].size();

        return horizontal(matrix, 0, end_col, 1);
    }

};

std::vector<int> Solution::horizontal(vector<vector<int>>& matrix, int start, int end, int dir) {
        std::vector<int> mat;

        int current_row = (dir > 0) ? start_row : (end_row - 1);
        int stop = (dir > 0) ? end : (end - 1);
        for (int x = start; x != stop; x+=dir) {
            mat.push_back(matrix[current_row][x]);
            std::cout << matrix[current_row][x];
        }
        std::vector<int> next;
        if (dir > 0){
            // Means we just finished the first movement
            // Next movement will be at the "last" column going downward (so adding to the row number)
            start_row++;
            if (start_row == end_row) {
                return mat;
            }
            next = vertical(
                matrix,
                start_row,
                end_row,
                1
            );
        }
        else {
            // Finished the third movement
            // Next movement will be going upwards on the first column
            end_row--;
            if (start_row == end_row) {
                return mat;
            }
            next = vertical(
                matrix,
                end_row - 1,
                start_col,
                -1
            );
        }

        mat.insert(mat.end(), next.begin(), next.end());
        return mat;
    }

std::vector<int> Solution::vertical(vector<vector<int>>& matrix, int start, int end, int dir) {
    std::vector<int> mat;
    int current_col = (dir > 0) ? (end_col - 1) : start_col;
    int stop = (dir > 0) ? end : end;
    for (int y = start; y != stop; y+=dir) {
        mat.push_back(matrix[y][current_col]);
        std::cout << matrix[y][current_col];
    }
    std::vector<int> next;
    if (dir > 0) {
        // double check if we've done all of the rows
        // Finished second movement, going backwards now
        end_col--;
        if (start_col == end_col) {
            return mat;
        }
        next = horizontal(
            matrix,
            (end_col - 1),
            start_col,
            -1
        );
    }
    else {
        start_col++;
        if (start_col == end_col) {
            return mat;
        }
        next = horizontal(
            matrix,
            start_col,
            end_col,
            1
        );
    }
    mat.insert(mat.end(), next.begin(), next.end());
    return mat;
}
