class Solution {
public:
    vector<vector<int>> findSubsequences1(vector<int>& nums) {
        set<vector<int>> sv;
        vector<int> v;
        solve(sv, v, 0, nums);
        vector<vector<int>> vv(sv.begin(), sv.end());
        return vv;
    }
    
    void solve(set<vector<int>> &sv, vector<int> &v, int i, vector<int> &nums){
        if(v.size()>=2){
            sv.insert(v);
        }
        for(int j=i;j<nums.size();++j){
            if(v.size()==0||v.back()<=nums[j]){
                v.push_back(nums[j]);
                solve(sv, v, j+1, nums);
                v.pop_back();
            }
        }
    }
    
    vector<vector<int>> findSubsequences(vector<int> &nums){
        set<vector<int>> sv;
        for(int i=0;i<nums.size();++i){
            set<vector<int>> st;
            for(vector<int> v:sv){
                if(v.back()<=nums[i]){
                    v.push_back(nums[i]);
                    st.insert(v);
                }
            }
            sv.insert(st.begin(), st.end());
            for(int j=0;j<i;++j){
                if(nums[j]<=nums[i]){
                    vector<int> tmp({nums[j], nums[i]});
                    sv.insert(tmp);
                }
            }
        }
        vector<vector<int>> ret(sv.begin(), sv.end());
        return ret;
    }
};
