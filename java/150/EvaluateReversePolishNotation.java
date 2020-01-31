class Solution {

    /** 使用集合来判断字符串是否为数字，代码可读性更好 */
    private static final Set<String> set = new HashSet<>(Arrays.asList("+", "-", "*", "/"));

    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (!set.contains(token)) {
                stack.push(Integer.parseInt(token));
            } else {
                int a = stack.pop();
                int b = stack.pop();
                if ("+".equals(token)) {
                    stack.push(b + a);
                } else if ("-".equals(token)) {
                    stack.push(b - a);
                } else if ("*".equals(token)) {
                    stack.push(b * a);
                } else {
                    stack.push(b / a);
                }
            }
        }
        return stack.pop();
    }
}