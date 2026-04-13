class MyQueue {
private:
    stack<int> stack_in, stack_out;

    // Helper to transfer elements only when the output stack is empty
    void move_if_needed() {
        if (stack_out.empty()) {
            while (!stack_in.empty()) {
                stack_out.push(stack_in.top());
                stack_in.pop();
            }
        }
    }
    
public:
    MyQueue() {}
    
    void push(int x) {
        stack_in.push(x);
    }
    
    int pop() {
        move_if_needed();
        int val = stack_out.top();
        stack_out.pop();
        return val;
    }
    
    int peek() {
        move_if_needed();
        return stack_out.top();
    }
    
    bool empty() {
        return stack_in.empty() && stack_out.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
