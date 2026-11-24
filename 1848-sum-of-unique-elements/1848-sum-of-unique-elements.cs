public class Solution {
    public int SumOfUnique(int[] nums) {
        Dictionary<int, int> counter = new Dictionary<int, int>();
        foreach(int num in nums) {
            if (!counter.ContainsKey(num)) {
                counter.Add(num, 0);
            }
            counter[num] += 1;
        }
        int sum = 0;
        foreach (var pair in counter) {
            if (pair.Value == 1) {
                sum += pair.Key;
            }
        }
        return sum;
    }
}