class AllOne {
public:
    /** Initialize your data structure here. */
    AllOne() {
        
    }
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        if(ms.find(key)==ms.end()){
            ms.insert(make_pair(key, 1));
            mi[1].insert(key);
        }
        else{
            mi[ms[key]].erase(key);
            if(mi[ms[key]].empty()){
                mi.erase(ms[key]);
            }
            ms[key]++;
            mi[ms[key]].insert(key);
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        if(ms.find(key)!=ms.end()){
            ms[key]--;
            if(ms[key]==0){
                ms.erase(key);
            }
            else{
                mi[ms[key]].insert(key);
            }
            mi[ms[key]+1].erase(key);
            if(mi[ms[key]+1].empty()){
                mi.erase(ms[key]+1);
            }
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        if(ms.empty()) return string("");
        return *(mi.rbegin()->second.begin());
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        if(ms.empty()) return string("");
        return *(mi.begin()->second.begin());
    }
    
private:
    map<string, int> ms;
    map<int, set<string>> mi;
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * string param_3 = obj.getMaxKey();
 * string param_4 = obj.getMinKey();
 */
