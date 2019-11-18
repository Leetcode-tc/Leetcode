class Solution {
public:
    string decodeString(string s) {
        int i = 0;
        return decodeString(s, i);
    }
    
    string decodeString(string &s, int &i){
        string ret;
        
        while(i<s.size()&&s[i]!=']'){
            if(isdigit(s[i])){
                int k = 0;
                while(i<s.size()&&isdigit(s[i])){
                    k = k*10 + (s[i]-'0');
                    i++;
                }
                i++;
                string tmp = decodeString(s, i);
                i++;
                while(k-->0)
                    ret += tmp;
            }
            else{
                ret += s[i++];
            }
        }
        
        return ret;
    }
};
