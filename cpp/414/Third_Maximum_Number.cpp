class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int> s;
        for(auto n:nums){
            s.insert(n);
            if(s.size()>3){
                s.erase(s.begin());
            }
        }
        return s.size()==3?*s.begin():*s.rbegin();
    }
};
