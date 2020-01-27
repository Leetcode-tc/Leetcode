class MyQueue {
    /** 两个栈，一个用来push（入队），一个用来pop（出队） */
    private Stack<Integer> stackForPush;
    private Stack<Integer> stackForPop;

    /** Initialize your data structure here. */
    public MyQueue() {
        stackForPush = new Stack<>();
        stackForPop = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        while (!stackForPop.isEmpty()) {
            stackForPush.push(stackForPop.pop());
        }
        stackForPush.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        shift();
        if (!stackForPop.isEmpty()) {
            return stackForPop.pop();
        }
        throw new RuntimeException("队列中无元素！");
    }
    
    /** Get the front element. */
    public int peek() {
        shift();
        if (!stackForPop.isEmpty()) {
            return stackForPop.peek();
        }
        throw new RuntimeException("队列中无元素！");
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stackForPop.isEmpty() && stackForPush.isEmpty();
    }

    /**
     * 辅助方法：将stackForPush中的元素全部倒入stackForPop中
     */
    private void shift() {
        if (stackForPop.isEmpty()) {
            while (!stackForPush.isEmpty()) {
               stackForPop.push(stackForPush.pop());
            }   
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */