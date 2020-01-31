class Solution {
    /**
     * 计算括号内的表达式值
     */
    private int evaluateExpr(Stack<Object> stack) {
        // 获取第一个操作数
        int res = (int) stack.pop();
        while (!stack.isEmpty() && !((char) stack.peek() == ')')) {
            char operator = (char) stack.pop();
            if (operator == '+') {
                res += (int) stack.pop();
            } else if (operator == '-') {
                res -= (int) stack.pop();
            }
        }
        return res;
    }

    public int calculate(String s) {
        // 用来存储操作数与操作符的栈
        // 涉及到存储int类型与char类型，必须用Object类型的栈
        Stack<Object> stack = new Stack<>();
        // 操作数占的位数
        int n = 0;
        // 操作数
        int operand = 0;
        
        // 倒序遍历字符串
        for (int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                operand = (int) Math.pow(10, n) * (ch - '0') + operand;
                n++;
            } else {
                // 将操作数入栈，并置为0
                if (n > 0) {
                    stack.push(operand);
                    n = 0;
                    operand = 0;
                }
                if (ch == '(') {
                    int res = evaluateExpr(stack);
                    // 将(出栈，将计算结果入栈
                    stack.pop();
                    stack.push(res);
                } else if (ch != ' ') {
                    stack.push(ch);
                }
            }
        }
        // 注意最后一个元素的处理
        if (n != 0) {
            stack.push(operand);
        }
        
        return evaluateExpr(stack);
    }
}