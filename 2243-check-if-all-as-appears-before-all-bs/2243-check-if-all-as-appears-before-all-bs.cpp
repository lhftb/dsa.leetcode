class Solution {
public:
    bool checkString(string s) {
        int i = -1;
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] == 'b') {
                i = j;
            }
            else if (i != -1) {
                return false;
            }
        }
        return true;
    }
};