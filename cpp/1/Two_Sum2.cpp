//
// Created by ryy on 2019-10-17.
//
#include <iostream>
#include <vector>
#include <map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result;
    map<int,int> numMap;
    int size = nums.size();
    for(int i = 0; i < size; i++){
        if(numMap.count(target - nums[i]) != 0 ){
            result.push_back(numMap[target - nums[i]]);
            result.push_back(i);
            break;
        }
        numMap[nums[i]] = i;
    }
    return result;
}