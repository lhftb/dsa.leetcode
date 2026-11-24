public class Solution {
    public int LongestOnes(int[] nums, int k) {
        int longest = 0;
        int zeroes  = 0;
        int i       = 0;
        for (int j = 0; j < nums.Length; ++j) {
            if (nums[j] == 0) {
                zeroes += 1;
            }
            while (i <= j && zeroes > k) {
                if (nums[i] == 0) {
                    zeroes -= 1;
                }
                i += 1;
            }
            longest = Math.Max(longest, j - i + 1);
        }
        return longest;
    }
}