//
// Created by ryy on 2019-11-27.
//
class Solution {
public:

    static bool cmp(vector<int> v1,vector<int> v2){
        if(v2[0] == v1[0])
            return v1[1] > v2[1];
        else
            return v1[0] < v2[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals){
        if(intervals.size() == 0 || intervals.size() == 1)   return intervals;
        vector<vector<int>> res;
        sort(intervals.begin(),intervals.end(),cmp);
        vector<int> tmp;
        tmp.push_back(intervals[0][0]);
        tmp.push_back(intervals[0][1]);
        res.push_back(tmp);
        int num = 0;
        int size = intervals.size();
        for(int i = 1; i < size; i++){
            if(intervals[i][0] <= res[num][1]) {
                res[num][1] = max(res[num][1], intervals[i][1]);
            }else{
                num++;
                tmp.clear();
                tmp.push_back(intervals[i][0]);
                tmp.push_back(intervals[i][1]);
                res.push_back(tmp);
            }
        }
        return res;
    }
};
