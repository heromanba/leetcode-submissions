/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> ret = new ArrayList<>();
        
        if(root==null)
            return ret;
        
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        
        while(!stack.isEmpty()) {
            Node curr = stack.pop();
            ret.add(curr.val);
            for(int i=0; i<curr.children.size(); i++)
                stack.push(curr.children.get(curr.children.size()-i-1));
        }
        return ret;
    }
}
