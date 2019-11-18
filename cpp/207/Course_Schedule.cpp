class Solution {
public:
    //拓扑排序,判断是否为有向无环图
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> m(numCourses);
        vector<int> indegree(numCourses);
        queue<int> q;
        
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
            for(auto v:m[w]){
                if(--indegree[v]==0)
                    q.push(v);
            }
        }
        
        //return all_of(indegree.begin(), indegree.end(), [](int degree){return degree==0;});
        return accumulate(indegree.begin(), indegree.end(), 0)==0;
    }
};
