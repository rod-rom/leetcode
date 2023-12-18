#include <vector>
#include <unordered_map>
  

class Solution {
public: 
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (m.count(complement)) {
                return {i, m[complement]};
            }
            m[nums[i]] = i;
        }

        return {};                   // No solution found

    }
};



