class MinStack {
    private Stack<Integer> stack;
    /** 栈顶保存当前的最小值 */
    private Stack<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int x) {
        stack.push(x);
        if (minStack.isEmpty()) {
            minStack.push(x);
        } else {
            // 注意等号，如果等于最小值的时候不做入栈处理，出栈时就会抛异常
            if (x <= minStack.peek()) {
                minStack.push(x);
            }
        }
    }
    
    public void pop() {
        int top = stack.pop();
        if (top == minStack.peek()) {
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
