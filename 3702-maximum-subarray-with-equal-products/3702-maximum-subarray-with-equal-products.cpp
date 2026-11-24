class Solution {
public:
    int maxLength(vector<int>& nums) {
        int len = 0;
        for (int i = 0; i < nums.size(); ++i) {
            long long prod = nums[i];
            long long vgcd = nums[i];
            long long vlcm = nums[i];
            for (int j = (i + 1); j < nums.size(); ++j) {
                prod = prod * nums[j];
                vgcd = gcd(vgcd, nums[j]);
                vlcm = lcm(vlcm, nums[j]);
                if (prod > vgcd * vlcm) {
                    break;
                }
                if (prod == vgcd * vlcm) {
                    len = max(len, j - i + 1);
                }
            }
        }
        return len;
    }
};