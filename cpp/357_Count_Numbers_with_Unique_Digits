class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if(n==0) return 1;
        int ret = 10;
        int currentProduct = 9;
        int a = 9;
        while(n-->1&&a>0){
            currentProduct *= a;
            a--;
            ret += currentProduct;
        }
        return ret;
    }
};
