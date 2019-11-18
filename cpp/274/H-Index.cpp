class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int n = citations.size();
        int i = n-1;
        while(i>=0){
            if(n-i>citations[i]){
                break;
            }
            i--;
        }
        return n-i-1;
    }
    
    //bucket sort
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> bucket(n+1, 0);
        for(int a:citations){
            if(a>=n){
                bucket[n]++;
            }
            else{
                bucket[a]++;
            }
        }
        int sum = 0;
        for(int i=n;i>=0;--i){
            sum += bucket[i];
            if(sum>=i){
                return sum;
            }
        }
        
        return 0;
    }
};
