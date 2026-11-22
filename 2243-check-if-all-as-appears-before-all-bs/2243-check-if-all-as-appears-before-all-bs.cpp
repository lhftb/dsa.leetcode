class Solution {
public:
    bool checkString(string s) {
        bool found = false;
        for (const auto& ch : s) {
            if (ch == 'b') {
                found = true;
            }
            else if (found) {
                return false;
            }
        }
        return true;
    }
};