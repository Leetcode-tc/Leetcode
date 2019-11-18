class Solution {
public:
    //广度优先搜索
    //          17    
    //减去小于自己的平方数 i^2 for i from [4..1]
    //得到    1  8  13  16
    int numSquares(int n) {
        int ret = 0, last = n;
        deque<int> q;
        q.push_back(n);
        while(!q.empty()){
            int t = q.front();
            q.pop_front();
            int i = int(sqrt(t));
            if(i*i==t){
                ret++;
                break;
            }
            while(i>0){
                q.push_back(t-i*i);
                i--;
            }
            if(t==last){
                ret++;
                last = q.back();
            }
        }
        
        return ret;
    }
};
