class Solution {
public:
    string reverseWords(string s) {
        int i = 0;
        int j = 0;
        while (j < s.size()) {
            if (s[j + 1] == ' ' || (j + 1) == s.size()) {
                int k = j;
                while (i < k) {
                    swap(s[i++], s[k--]);
                }
            }
            while (s[j] == ' ') {
                j += 1;
                i  = j;
            }
            j += 1;
        }
        return s;
    }
};