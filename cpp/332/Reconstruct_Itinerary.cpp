class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        map<string, multiset<string>> m;
        vector<string> ret;
        
        for(auto p:tickets){
            m[p.first].insert(p.second);
        }
        dfs(m, ret, "JFK");
        
        return vector<string>(ret.rbegin(), ret.rend());
    }
    //最后各个站点会连成一条线，所以只需深度优先搜索一次，当一个站点没有相邻未访问节点的时候，表示它后面的路径都已经遍历，将它记录，就是倒数第k个站点
    void dfs(map<string, multiset<string>> &m, vector<string> &ret, string s){
        while(!m[s].empty()){
            string a = *(m[s].begin());
            m[s].erase(m[s].begin());
            dfs(m, ret, a);
        }
        ret.push_back(s);
    }
};
