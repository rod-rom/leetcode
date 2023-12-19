class Solution {
    public:
        bool isValid(string s) {
            unordered_map<char, char> map = {{'(', ')'}, {'{', '}'}, {'[', ']'}}
            stack<char> stack;
            if (s.size() % 2 != 0) return false;
            for (char c : s) {
                 if (!stack.empty()) {
                    char prev = stack.top();
                    stack.push(c);
                    if (map[prev] == stack.top()) {
                        // remove the pair 
                        stack.pop();
                        stack.pop();
                    }
                 } else {
                        stack.push(c);
                 }
            }
            return stack.empty(); 
        }
};

