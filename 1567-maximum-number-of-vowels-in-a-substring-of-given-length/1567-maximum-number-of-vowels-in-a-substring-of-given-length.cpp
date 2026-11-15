class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int                 count = count_if(s.begin(), s.begin() + k, [&](const char& c) -> bool { return vowels.find(c) != vowels.end(); });
        int                 res   = count; 
        for (int j = k; j < s.size(); ++j)  {
            if (vowels.find(s[j]) != vowels.end()) {
                count += 1;
            }
            if (vowels.find(s[j - k]) != vowels.end()) {
                count -= 1;
            }
            res = max(res, count);
        }
        return res;
    }
};