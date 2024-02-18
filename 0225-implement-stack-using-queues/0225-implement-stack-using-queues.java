class MyStack {

    List<Integer> stack;
    
    public MyStack() {
        stack = new ArrayList();
    }
    
    public void push(int x) {
        this.stack.add(x);
    }
    
    public int pop() {
        int tar = this.stack.get(this.stack.size() - 1);
        this.stack.remove(this.stack.size()- 1);
        return tar;
    }
    
    public int top() {
        return this.stack.get(this.stack.size() - 1);
    }
    
    public boolean empty() {
        return this.stack.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */