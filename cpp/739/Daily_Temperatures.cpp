class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> v(T.size(), 0);
        vector<int> b(101, 30000);
        for(int i=T.size()-1;i>=0;--i){
            for(int k=T[i]+1;k<101;++k){
                if(b[k]!=30000 && (v[i]==0 || b[k]-i<v[i])){
                    v[i] = b[k]-i;
                }
                 
            }
            b[T[i]] = i;
        }
        return v;
    }
};