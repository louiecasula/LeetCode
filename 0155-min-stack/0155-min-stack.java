class MinStack {

    Stack<Integer> stack;
    TreeMap<Integer, Integer> treeMap;

    public MinStack() {
        stack = new Stack();
        treeMap = new TreeMap();
    }
    
    public void push(int val) {
        Integer iVal = Integer.valueOf(val);
        stack.push(iVal);
        if (treeMap.containsKey(iVal)) { treeMap.put(iVal, treeMap.get(iVal) + 1); }
        else { treeMap.put(iVal, 1); }
    }
    
    public void pop() {
        Integer val = stack.pop();
        if (treeMap.get(val) == 1) { treeMap.remove(val); }
        else { treeMap.put(val, treeMap.get(val) - 1); }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return treeMap.firstKey();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */