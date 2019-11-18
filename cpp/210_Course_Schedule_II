class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> m(numCourses);
        vector<int> indegree(numCourses, 0);
        queue<int> q;
        vector<int> ret;
        
        for(auto p:prerequisites){
            m[p.second].push_back(p.first);
            indegree[p.first]++;
        }
        
        for(int i=0;i<numCourses;++i){
            if(indegree[i]==0)
                q.push(i);
        }
        
        while(!q.empty()){
            int w = q.front();
            q.pop();
            
            ret.push_back(w);
            for(auto v:m[w]){
                if(--indegree[v]==0)
                    q.push(v);
            }
        }
        
        if(all_of(indegree.begin(), indegree.end(), [](int t){return t==0;})==false)
            ret.clear();
        return ret;
    }
};
