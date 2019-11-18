class Solution {
public:
    //尽量分配给需求小的孩子
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int i=0, j=0;
        for(j=0;j<s.size()&&i<g.size();++j)
            if(s[j]>=g[i])
                i++;
        return i;
    }
};
