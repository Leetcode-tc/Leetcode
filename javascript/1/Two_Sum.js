/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    map = {};
    ret = [];
    var i = 0;
    while(i<nums.length){
        if(map[nums[i]]){
            ret.push(map[nums[i]]);
            ret.push(i+1);
            break;
        }
        else{
            map[target-nums[i]] = i+1;
        }
        i++;
    }
    return ret;
};