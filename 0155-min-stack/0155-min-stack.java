class MinStack {

    List<int[]> stackArray;

    public MinStack() {
        stackArray = new ArrayList<>();
    }
    
    public void push(int val) {
        if (stackArray.size() == 0) { 
            stackArray.add(new int[] { val, val });
            return;
        }
        int[] top = stackArray.get(stackArray.size() - 1);
        // Save min val reached so far at each element in arraylist
        if (top[1] > val) {
            stackArray.add(new int[] { val, val });
        } else {
            stackArray.add(new int[] { val, top[1] });
        }
    }
    
    public void pop() {
        if (stackArray.size() == 0) { return; }
        stackArray.remove(stackArray.size() - 1);
    }
    
    public int top() {
        if (stackArray.size() == 0) { return -1; }
        return stackArray.get(stackArray.size() - 1)[0];
    }
    
    public int getMin() {
        if (stackArray.size() == 0) { return -1; }
        return stackArray.get(stackArray.size() - 1)[1];
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