class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int count = 0;
        int rows = mat.size();
        int cols = mat[0].size(); // Assuming all rows have the same number of columns

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (mat[i][j] == 1) {
                    bool left = false, right = false, up = false, down = false;

                    for (int left_ = j - 1; left_ >= 0; left_--) {
                        if (mat[i][left_] == 1) {
                            left = true;
                            break;
                        }
                    }

                    for (int right_ = j + 1; right_ < cols; right_++) {
                        if (mat[i][right_] == 1) {
                            right = true;
                            break;
                        }
                    }

                    for (int up_ = i - 1; up_ >= 0; up_--) {
                        if (mat[up_][j] == 1) {
                            up = true;
                            break;
                        }
                    }

                    for (int down_ = i + 1; down_ < rows; down_++) {
                        if (mat[down_][j] == 1) {
                            down = true;
                            break;
                        }
                    }

                    if (up==false && down==false && right==false && left==false) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
};
