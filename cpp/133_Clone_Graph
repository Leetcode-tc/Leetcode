/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if(!node) return NULL;
        return clone(node);
    }
    //深度优先搜索
    UndirectedGraphNode *clone(UndirectedGraphNode *node){
        if(clonedNodesMap.find(node)!=clonedNodesMap.end())
            return clonedNodesMap[node];
        UndirectedGraphNode *newNode = new UndirectedGraphNode(node->label);
        clonedNodesMap[node] = newNode;
        for(UndirectedGraphNode *neighbor:node->neighbors){
            newNode->neighbors.push_back(clone(neighbor));
        }
        return newNode;
    }

private:
    map<UndirectedGraphNode*,UndirectedGraphNode*> clonedNodesMap;
};
