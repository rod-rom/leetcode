class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> count;
        if (s.size() != t.size()) { return false; }
        
        // Count the frequecy for string s 
        for (auto x : s) {
            cout[s]++;
        }

        // Decrease the frequency for string t 
        for (auto y : t){
            count[y]--;
        }

        // find if counts are zero
        for (auto z : count) {
            if (z.second != 0) {
                return false;
            }
        }
        return true;
    }
}
