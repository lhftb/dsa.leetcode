class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int min_len = nums.size() + 1;
        int i       = 0;
        int sum     = 0;
        for (int j = 0; j < nums.size(); ++j) {
            sum += nums[j];
            while (i <= j && sum >= target) {
                min_len = min(min_len, j - i + 1);
                sum    -= nums[i++];
            }
        }
        return min_len > nums.size() ? 0 : min_len;
    }
};