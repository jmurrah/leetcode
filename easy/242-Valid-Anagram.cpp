// Given two strings s and t, return true if t is an anagram of s, and false otherwise.


class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) {
            return false;
        }

        std::unordered_map<char, int> sMap;
        std::unordered_map<char, int> tMap;

        for(int i=0; i < s.size(); i++) {
            sMap[s[i]] += 1;
            tMap[t[i]] += 1;
        }

        for (const auto& p : sMap) {
            if(sMap[p.first] != tMap[p.first]) {
                return false;
            }
        }
        return true;
    }
};
