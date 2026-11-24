public class Solution {
    public string FrequencySort(string s) {
        char[] chars = s.ToCharArray();
        Dictionary<char, int> freqs = new Dictionary<char, int>();
        foreach (char c in chars) {
            if (!freqs.ContainsKey(c)) {
                freqs.Add(c, 0);
            }
            freqs[c] += 1;
        }
        Array.Sort(chars, (a, b) => {
            int cmp =  freqs[b].CompareTo(freqs[a]);
            if (cmp == 0) {
                return a.CompareTo(b);
            }
            return cmp;
        }
        );
        return new string(chars);
    }
}