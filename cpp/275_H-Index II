class Solution {
public:
    int hIndex(vector<int>& citations) {
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
};
