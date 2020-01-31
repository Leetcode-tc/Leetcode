class Solution {

    private static Map<Character, Character> mappings = new HashMap<Character, Character>();
 
    static {
        mappings.put(')', '(');
        mappings.put(']', '[');
        mappings.put('}', '{');
    }

    /**
     * 标准答案写得太优雅了，借鉴过来了
     * 1)栈空时给topElement赋值，省去了单独对栈空情况做逻辑
     * 2)map中把后括号作为key，可直接用get获取前括号进行匹配
     * 3)根据key取value的逻辑，减少一次分支执行
     * 同时，修复了标准答案中empty()与isEmpty()使用不一致的问题
     * 
     * @param s 输入的字符串
     * @return 括号是否匹配成功
     */
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (mappings.containsKey(c)) {
                char topElement = stack.isEmpty() ? '#' : stack.pop();
                if (topElement != mappings.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
