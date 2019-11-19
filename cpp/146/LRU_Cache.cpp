class LRUCache {
    int cap;
    unordered_map<int, list<pair<int, int>>::iterator> um;
    list<pair<int, int>> lp;
public:
    LRUCache(int capacity) : cap(capacity){
        
    }
    
    int get(int key) {
        auto pi = um.find(key);
        //not found
        if(pi==um.end()) {
            return -1;
        }
        moveToFirst(um[key]);
        return lp.begin()->second;
    }
    
    void put(int key, int value) {
        auto pi = um.find(key);
        if(pi==um.end()) {
            //if capacity is out, erase the LRU one
            if(um.size()>=cap) {
                auto pt = lp.rbegin();
                um.erase(pt->first);
                lp.pop_back();
            }
            //add the <key, value> pair to front anyway
            lp.push_front(make_pair(key, value));
            um[key] = lp.begin();
        }
        else {
            pi->second->second = value;
            moveToFirst(pi->second);
        }
    }

    /*
     remove the element pointed by it(iterator)
     and add it to the front
     */
    void moveToFirst(list<pair<int, int>>::iterator it) {
        pair<int, int> np = *it;
        lp.erase(it);
        lp.push_front(np);
        um[np.first] = lp.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */