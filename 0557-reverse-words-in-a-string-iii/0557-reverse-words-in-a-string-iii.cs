public class Solution {
    public string ReverseWords(string s) {
        char[] chars = s.ToCharArray();
        int i = 0;
        int j = 0;
        while (j < s.Length) {
            if (s[j] == ' ') {
                j += 1;
                i  = j;
                continue;
            }
            if (j == (s.Length - 1) || s[j + 1] == ' ') {
                int k = j;
                while (i < k) {
                    (chars[i], chars[k]) = (chars[k], chars[i]);
                    i += 1;
                    k -= 1;
                }
            }
            j += 1;
        }
        return new string(chars);
    }
}