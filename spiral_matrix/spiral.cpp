#include <iostream>
#include <stdlib.h>
#include <vector>

std::vector<std::vector<int>> matrix;
auto start_row = 0;
auto start_col = 0;
int end_row;
int end_col;

std::vector<int> horizontal(int start, int end, int dir);
std::vector<int> vertical(int start, int end, int dir);

std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
    end_row = matrix.size();
    end_col = matrix[0].size();
    std::cout << end_row << "r " << end_col << "c " << std::endl;
    return horizontal(0, end_col, 1);
}

std::vector<int> horizontal(int start, int end, int dir) {
    std::vector<int> mat;
    auto current_row = (dir > 0) ? start_row : (end_row - 1);
    auto stop = (dir > 0) ? end : (end - 1);
    for (auto x = start; x != stop; x+=dir) {
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
            end_row - 1,
            start_col,
            -1
        );
    }
    mat.insert(mat.end(), next.begin(), next.end());
    return mat;
}

std::vector<int> vertical(int start, int end, int dir) {
    std::vector<int> mat;
    auto current_col = (dir > 0) ? (end_col - 1) : start_col;
    auto stop = (dir > 0) ? end : end;
    for (auto y = start; y != stop; y+=dir) {
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
            start_col,
            end_col,
            1
        );
    }
    mat.insert(mat.end(), next.begin(), next.end());
    return mat;
}

void print_vector(std::vector<int> vec) {
    for (auto e : vec) {
        std::cout << e << " ";
    }
    std::cout << std::endl;
}

int main() {
    matrix = {
        {1,2,3,4},
        {5,6,7,8},
        {9,8,10,11}
    };
    auto flat = spiralOrder(matrix);
    std::cout << std::endl;
    print_vector(flat);
    matrix = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    auto flat2 = spiralOrder(matrix);
    std::cout << std::endl;
    print_vector(flat2);

    return 0;
}
