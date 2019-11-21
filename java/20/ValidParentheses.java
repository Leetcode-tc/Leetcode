import java.util.Stack;

/**
 * @author: create by nadao
 * @version: v1.0
 * @description: 有效的括号
 * @date:2019/11/19
 */
public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> mark = new Stack<>();
        for(char cur : s.toCharArray()){
            if(cur == '(' || cur == '[' || cur == '{' ){
                mark.push(cur);
            }
            if(cur == ')' || cur == ']' || cur == '}'){
                if(mark.isEmpty()) {
                    return false;
                }
                char p = mark.pop();
                if (cur == ')' && p != '('){
                    return false;
                }
                if (cur == ']' && p != '['){
                    return false;
                }
                if (cur == '}' && p != '{'){
                    return false;
                }
            }
        }
        return mark.isEmpty();
    }
}
