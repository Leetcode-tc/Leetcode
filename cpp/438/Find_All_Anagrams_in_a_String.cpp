class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ret;
        vector<int> m(128, 0);
        for(auto c:p){
            m[c]++;
        }
        
        int count = p.size();
        int begin = 0, end = 0;
        while(end<s.size()){
            if(m[s[end++]]-->0) count--;
            if(count==0) ret.push_back(begin);
            if(end-begin==p.size()&&m[s[begin++]]++>=0) count++;
        }
        
        return ret;
    }
};
