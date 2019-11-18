class Solution {
public:
    //根据气球结束位置从小到大排序，从当前位置开始，尽量往右射箭，即选择距离当前最近的气球，将它的结束位置作为下一支箭的位置
    //
    //        --------    ------------    ------ ------
    //    --------    ----    ------------       -----------
    //------------------------------------------------------------->
    //1   2   3   4   5   6   7   8   9   10    11    12    13    14
    //            ^       ^                ^           ^
    //如上图所示，气球位置排序后为[[2,4],[3,5],[5,6],[6,9],[7,10],[10,11],[11,12],[11,13]]
    //第一步，需要把[2,4]射破，所以在4的位置放一支箭，[3,5]也被射破；
    //第二步，射破[5,6],[6,9]也随之解决；
    //第三步，射破[7,10],[10,11]也随之解决；
    //第四步，射破[11,12],[11,13]也随之解决；
    //共需4支箭
    int findMinArrowShots(vector<pair<int, int>>& points) {
        if(points.size()==0) return 0;
        sort(points.begin(), points.end(), [](pair<int, int> p1, pair<int, int> p2){
            return p1.second<p2.second;
        });
        int ret = 1;
        int currentPos = points[0].second;
        for(int i=1;i<points.size();++i){
            if(points[i].first<=currentPos) continue;
            currentPos = points[i].second;
            ret++;
        }
        return ret;
    }
};
