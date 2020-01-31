//
// Created by 任银垠 on 2020-01-29.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> prevPermOpt1(vector<int>& A) {
    int size = A.size();
    if(size <= 1) return A;
    int big_pos = -1;
    int big = A[size-1];
    //从后往前寻找第一个逆序的位置及其值
    for(int i = size-1; i > 0; i--){
        if(A[i] < A[i-1]){
            big_pos = i-1;
            big = A[i-1];
            break;
        }
    }
    //如果位置没有更新，代表无逆序，直接返回A
    if(big_pos == -1) return A;
    int small = A[big_pos+1];
    int small_pos = big_pos+1;
    //从找到的逆序位置往后寻找小于该值的最左最大的值
    for(int j = big_pos+1; j < A.size(); j++){
        if(A[j] > small && A[j] < big){
            small = A[j];
            small_pos = j;
        }
    }
    swap(A[big_pos], A[small_pos]);
    return A;
}

int main(){
    vector<int> vec = {1,9,4,6,7};
    vector<int> res = prevPermOpt1(vec);
    for(auto i:res){
        cout<<i<<endl;
    }
    return 0;
}