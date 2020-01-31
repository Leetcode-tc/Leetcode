class Solution {
    public int calPoints(String[] ops) {
        Stack<Integer> stack = new Stack<>();
        for (String str : ops) {
            if ("+".equals(str)) {
                int top = stack.pop();
                int newTop = top + stack.peek();
                stack.push(top);
                stack.push(newTop);
            } else if ("D".equals(str)) {
                stack.push(stack.peek() * 2);
            } else if ("C".equals(str)) {
                stack.pop();
            } else {
                stack.push((Integer.valueOf(str))); 
            }
        }
        int res = 0;
        for(int score : stack) res += score;
        return res;
    }
}