class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> map;
        for(int x = 0; x < nums.size(); x++) {
            if (map.find(target - nums[x]) != map.end())
                return {map[target - nums[x]] , x};
            map[nums[x]] = x;
        }
        return vector<int>{0,0};
    }
};
