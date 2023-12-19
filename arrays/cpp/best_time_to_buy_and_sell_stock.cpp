class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int l = 0;
        int r = 0;
        while (r < prices.size()) {
            // potential profit
            if (prices[l] < prices[r]) {
                maxProfit = max(maxProfit, prices[r] - prices[l]);
            } else {
                l = r;
            }
            ++r;
        }
        return maxProfit;
    }
};
