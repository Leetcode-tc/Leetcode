class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int Asum = accumulate(A.begin(), A.end(), 0);
        int startNum = 0;
        int n = A.size();
        for(int i=0;i<n;++i){
            startNum += i*A[i];
        }
        int ret = startNum;
        for(int i=n-1;i>0;--i){
            startNum += Asum-n*A[i];
            if(startNum>ret){
                ret = startNum;
            }
        }
        return ret;
    }
};
