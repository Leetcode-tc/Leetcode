/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 实现strStr()
 * @date:2019/11/19
 */
public class ImplementstrStr {
    public int strStr(String haystack, String needle) {
        if(needle == "") return 0;
        for (int i = 0; i <= haystack.length()-needle.length(); i++) {
            if(haystack.substring(i,i+needle.length()).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}
