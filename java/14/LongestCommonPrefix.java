/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 最长公共前缀
 * @date:2019/11/19
 */
public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if(strs==null || strs.length==0){
            return "";
        }
        String res = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (strs[i].indexOf(res) != 0){
                res = res.substring(0,res.length()-1);
            }
        }
        return res;
    }
}
