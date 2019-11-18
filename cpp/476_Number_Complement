class Solution {
public:
    int findComplement(int num) {
        //~11111000 ^ 00000101 = 00000010 
        unsigned int prefix = 1<<31;
        cout << (num&prefix) << endl;
        while((num&prefix)==0)
            prefix = (prefix>>1) + (1<<31);
        prefix <<= 1;
        return ~prefix^num;
    }
};
