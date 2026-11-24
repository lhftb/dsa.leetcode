public class Solution {
    public string ReverseOnlyLetters(string s) {
        char[] chars = s.ToCharArray();
        int    i     = 0;
        int    j     = s.Length - 1;
        while (i < j) {
            if (!(s[i] >= 'a' && s[i] <= 'z') && !(s[i] >= 'A' && s[i] <= 'Z')) {
                i += 1;
                continue;
            }
            if (!(s[j] >= 'a' && s[j] <= 'z') && !(s[j] >= 'A' && s[j] <= 'Z')) {
                j -= 1;
                continue;
            }
            (chars[i], chars[j]) = (chars[j], chars[i]);
            i += 1;
            j -= 1;
        }
        return new string(chars);
    }
}