class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        stack<int> s;
        unordered_map<int, int> m;
        
        for(auto n:nums){
            while(!s.empty()&&s.top()<n){
                m[s.top()] = n;
                s.pop();
            }
            s.push(n);
        }
        
        for(auto &n:findNums){
            n = m.find(n)!=m.end()?m[n]:-1;
        }
        
        return findNums;
    }
};
