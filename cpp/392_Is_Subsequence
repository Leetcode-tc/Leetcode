class Solution {
public:
    bool isSubsequence(string s, string t) {
        map<char, vector<int>> m;
        for(int i=0;i<t.size();++i){
            m[t[i]].push_back(i);
        }
        return isSubsequence(s, m);
    }
    //遍历s，令当前字符为c，在t中从上一位置开始，找到第一个和c相同的字符，然后继续
    //如果输入多个s，可以用一个map记录下t中各个字符出现的位置数组，然后对于每一个c，在m[c]中进行二分查找
    //用dp记录每一个字符上一次的位置后面一个，往后只要从这里开始找
    //s="acbc",t="ahwbcaeacbc"
    //具有map: 'a'->[0, 5, 7, 11]
    //         'b'->[3, 9]
    //         'c'->[4, 8, 10]
    //         ...
    //dp[x]记录了上一次在m[x]上找到符合条件的数的下一位置，也就是下一次在m[x]上查找开始的位置
    //p记录了s[i]的上一个字符s[i-1]在t中的位置，s[i]需要大于p的位置出现才符合条件，即m[s[i]]数组中有大于p的值
    //第一步：c = 'a', dp['a'] = 0, p = -1,在m['a']的0-3位置找第一个比p大的数，找到0
    //      更新  p = 0, dp['a'] = 1
    //第二步：c = 'c', dp['c'] = 0, p = 0,在m['c'](0,2)找第一个比p大的数，为4
    //      更新  p = 4, dp['c'] = 1
    //第三步：c = 'b', dp['b'] = 0, p = 4,在m['b'](0,0)找第一个比p大的数，为9
    //      更新  p = 9, dp['b'] = 2
    //第四步：c = 'c', dp['c'] = 1, p = 9,在m['c'](1,2)找第一个比p大的数，为10
    //      更新  p = 10, dp['c'] = 3
    //结束，s遍历完，返回true，如果没有找到m[c]中大于p的位置，则直接结束，返回false
    bool isSubsequence(string s, map<char, vector<int>> &m){
        int dp[26] = {0};
        int p = -1;
        for(auto c:s){
            dp[c-'a'] = findNextPos(m[c], p, dp[c-'a']);
            if(dp[c-'a']==0)
                return false;
            p = m[c][dp[c-'a']-1];
        }
        return true;
    }
    
    int findNextPos(vector<int> &v, int n, int l){
        int ret = -1;
        int r = v.size()-1;
        while(l<=r){
            int mid = l+(r-l)/2;
            if(v[mid]<n)
                l = mid+1;
            else if(v[mid]>n)
                r = mid-1;
        }
        if(l<v.size())
            ret = l;
        return ret+1;
    }
};
