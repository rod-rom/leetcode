class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> seen;
        for (auto n: nums) {
            if (seen[n] == true) {
                return true;
            } else {
                seen[n] = true;
            }
        }
        return false;
    }
}

