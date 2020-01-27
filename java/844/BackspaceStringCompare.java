class Solution {
    public boolean backspaceCompare(String S, String T) {
        return build(S).equals(build(T));
    }

    /**
     * 思路没问题，代码参考标准答案，更加优雅
     * 1.使用for-each结构与toCharArray方法结合，使代码更简洁；
     * 2.对栈使用String.valueOf方法，获取字符串的值
     */
    private String build(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch != '#') {
                stack.push(ch);
            } else if (!stack.isEmpty()) {
                stack.pop();
            }
        }
        return String.valueOf(stack);
    }
}