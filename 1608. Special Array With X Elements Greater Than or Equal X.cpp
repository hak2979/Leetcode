class Solution {
public:
    int specialArray(std::vector<int>& nums) {
    int max_val = *std::max_element(nums.begin(), nums.end());
    std::vector<int> n1(max_val + 1, 0);

    for(int i_out = 0; i_out <= max_val; i_out++){
        for(int i = 0; i < nums.size(); i++){
            if(i_out <= nums[i]){
                n1[i_out] += 1;
            }
        }
    }

    for(int i = 0; i <= max_val; i++){
        if(n1[i] == i){
            return i;
        }
    }

    return -1;
    }
};
