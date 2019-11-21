/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 罗马数字转成阿拉伯数字
 * @date:2019/11/19
 */
public class RomanToInteger {
    public int romanToInt(String s) {
        if (s == null || s.length() == 0){
            return 0;
        }
        int res = 0;
        if(s.contains("IV")){
            res -= 2;
        }
        if(s.contains("IX")){
            res -= 2;
        }
        if(s.contains("XL")){
            res -= 20;
        }
        if(s.contains("XC")){
            res -= 20;
        }
        if(s.contains("CD")){
            res -= 200;
        }
        if(s.contains("CM")){
            res -= 200;
        }
        for(char i : s.toCharArray()){
            if('M' == i){
                res += 1000;
            }
            if('D' == i){
                res += 500;
            }
            if('C' == i){
                res += 100;
            }
            if('L' == i){
                res += 50;
            }
            if('X' == i){
                res += 10;
            }
            if('V' == i){
                res += 5;
            }
            if('I' == i){
                res += 1;
            }
        }
        return res;
    }
}
