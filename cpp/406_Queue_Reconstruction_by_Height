class Solution {
public:
    //按身高从高到低排，然后依次遍历，此时前面都是比当前这个人高的，只需根据第二项的值插入相应位置就好
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        vector<pair<int, int>> ret;
        sort(people.begin(), people.end(), [](pair<int, int> pa, pair<int, int> pb){
            return pa.first!=pb.first?pa.first>pb.first:pa.second<pb.second;
        });
        for(auto p:people){
            ret.insert(ret.begin()+p.second, p);
        }
        return ret;
    }
};
