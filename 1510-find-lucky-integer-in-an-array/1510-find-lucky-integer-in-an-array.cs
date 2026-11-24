public class Solution {
    public int FindLucky(int[] nums) {
        Dictionary<int, int> freqs = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (!freqs.ContainsKey(num)) {
                freqs.Add(num, 0);
            }
            freqs[num] += 1;
        }
        int lucky = -1;
        foreach (var item in freqs) {
            if (item.Key == item.Value) {
                lucky = Math.Max(lucky, item.Key);
            }
        }
        return lucky;
    }
}