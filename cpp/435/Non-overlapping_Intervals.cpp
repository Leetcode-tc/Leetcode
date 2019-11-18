/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    //区间问题，按照区间结束位置排序，优先选择结束位置最小的区间，记录重叠的区间数量
    int eraseOverlapIntervals(vector<Interval>& intervals) {
        if(intervals.size()==0) return 0;
        int ret = 0;
        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b){
            return a.end<b.end;
        });
        int t = intervals[0].end;
        for(int i=1;i<intervals.size();++i){
            if(intervals[i].start<t) ret++;
            else t = intervals[i].end;
        }
        return ret;
    }
};
