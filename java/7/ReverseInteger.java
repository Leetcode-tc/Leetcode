/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 翻转数字
 * @date:2019/11/19
 */
public class ReverseInteger {
    public int reverse(int x) {
        int res = 0;
        while(x != 0){
            int newRes = res*10+x%10;
            if ((newRes-x%10)/10 != res){
                return 0;
            }
            res = newRes;
            x = x/10;
        }
        return res;
    }
}
