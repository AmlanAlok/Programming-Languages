public boolean ans(String s) {
        
    Deque<Character> stack = new LinkedList<>();
    
    for (char c: s.toCharArray()) {
        if (!stack.isEmpty()){
            if ((stack.peekLast() == '(' && c == ')') ||
                (stack.peekLast() == '{' && c == '}') ||
                (stack.peekLast() == '[' && c == ']')){
                stack.removeLast();
                continue;
            }
        }
        stack.addLast(c);
    }
    
    return stack.isEmpty();
}
