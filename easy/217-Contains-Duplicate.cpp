// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std:unordered_set<int> seen;

        for(int i=0; i < nums.size(); i++) {
            if(seen.find(nums[i]) != seen.end()) {
                return true;
            }
            seen.insert(nums[i]);
        }
        return false;
    }
};
