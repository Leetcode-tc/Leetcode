class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int ret = 0;
        int n = 0;
        for(int i=2;i<A.size();++i){
            if(A[i]-A[i-1]==A[i-1]-A[i-2]){
                n++;
                ret += n;
            }
            else{
                n = 0;
            }
        }
        return ret;
    }
    
    
    int numberOfArithmeticSlices(vector<int>& A) {
        if(A.size()<=2) return 0;
        int ret = 0;
        int p = 0, q = 1;
        int currentDiff = A[q]-A[p];
        while(q<A.size()-1){
            if(A[++q]-A[q-1]!=currentDiff){
                if(q-p>2){
                    ret += helper(q-p);
                }
                p = q-1;
                currentDiff = A[q]-A[p];
            }
        }
        if(q-p+1>2){
            ret += helper(q-p+1);
        }
        return ret;
    }
    
    
    int helper(int n){
        int ret = 0;
        for(int i=n;i>=3;--i){
            ret += n-i+1;
        }
        return ret;
    }
};
