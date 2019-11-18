class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        vector<string> ret;
        int sum = INT_MAX;
        map<string, int> m;
        
        for(int i=0;i<list1.size();++i){
            m[list1[i]] = i;
        }
        for(int i=0;i<list2.size();++i){
            if(m.find(list2[i])!=m.end()){
                int tmp = m[list2[i]]+i;
                if(tmp<sum){
                    sum = tmp;
                    ret.clear();
                    ret.push_back(list2[i]);
                }
                else if(tmp==sum){
                    ret.push_back(list2[i]);
                }
            }
        }
        
        return ret;
    }
};
