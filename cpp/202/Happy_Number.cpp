class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> us{n};
        bool ret = false;
        while(1){
            int t = 0;
            while(n>0){
                t += pow(n%10, 2);
                n /= 10;
            }
            if(t==1||us.find(t)!=us.end()){
                ret = t==1?true:false;
                break;
            }
            n = t;
            us.insert(n);
        }
        return ret;
    }
};
