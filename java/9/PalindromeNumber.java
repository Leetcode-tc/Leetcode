/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 判断是否为回文数
 * @date:2019/11/19
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if(x<0 || (x>0 && x%10==0)){
            return false;
        }
        int palind = x;
        int res = 0;
        while (x != 0){
            res = res*10 + x%10;
            x = x/10;
        }
        return palind == res;
    }
}
