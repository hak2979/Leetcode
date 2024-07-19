class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        string to_find = "";
        
        for (int i = 0; i < paths.size(); i++) {
            if (to_find.empty()) {
                to_find = paths[i][1];
                i=0;
            } else {
                if (paths[i][0] == to_find) {
                    to_find = paths[i][1];
                    i=0;
                }
            }
        }
        return to_find;
    }
};
