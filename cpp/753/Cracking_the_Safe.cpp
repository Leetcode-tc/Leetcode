class Solution {
public:
    string crackSafe(int n, int k) {
        string curStr(n, '0');
        unordered_set<int> us({0});
        int len = pow(k, n)+n-1;
        dfs(us, n, k, len, curStr);
        return curStr;
    }

    bool dfs(unordered_set<int> &us, int n, int k, int len, string &curStr){
        if(curStr.size()==len){
            return true;
        }
        int base = pow(10, n-1);
        int newStr = stoi(curStr.substr(curStr.size()-n, n));
        newStr %= base;
        for(int i=0;i<k;++i){
            newStr = newStr*10+i;
            if(us.find(newStr)==us.end()){
                us.insert(newStr);
                curStr.push_back('0'+i);
                //剪枝
                if(dfs(us, n, k, len, curStr)){
                    return true;
                }
                //回溯
                curStr.pop_back();
                us.erase(newStr);
            }
            newStr /= 10;
        }
        return false;
    }
};