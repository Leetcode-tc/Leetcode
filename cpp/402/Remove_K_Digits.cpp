class Solution {
public:
    //从前往后寻找，当num[i]>num[i-1]时，删除i，比如
    //1432219,num[1]=4>num[2]=3,删除4，得到132219，这是删除1个数字得到最小的数
    //10200,删除1个得到0200,需要将开头的0去掉
    //123456,这种情况删除最后一个
    string removeKdigits(string num, int k) {
        if(num.size()==k) return "0";
        int lastDeletePos = 1;
        while(k-->0){
            int i;
            for(i=lastDeletePos;i<num.size()&&num[i]>=num[i-1];++i);
            lastDeletePos = i-1;
            num.erase(lastDeletePos, 1);
        }
        int i=0;
        while(i<num.size()&&num[i]=='0')
            i++;
        return num.size()==i?"0":num.substr(i, num.size()-i);
    }
    //上一种方法频繁从string里删除非末尾字符，耗费时间，这里用一个辅助字符串来存储结果，可以提高效率
    string removeKdigits(string num, int k) {
        if(num.size()==k) return "0";
        string ret;
        for(int i=0;i<num.size();){
            if(ret.size()>0&&ret.back()>num[i]&&k>0){
                ret.pop_back();
                k--;
            }
            else{
                ret.push_back(num[i]);
                i++;
            }
        }
        ret = ret.substr(0, ret.size()-k);
        int i=0;
        while(i<ret.size()&&ret[i]=='0')
            i++;
        return ret.size()==i?"0":ret.substr(i, ret.size()-i);
    }
};
