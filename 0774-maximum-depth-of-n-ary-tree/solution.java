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
    public int maxDepth(Node root) {
        int ret = 0;
        if(root==null)
            return ret;
        List<Node> curr=new ArrayList<>(1);
        curr.add(root);
        while(!curr.isEmpty()){
            ret++;
            int size=0;
            for(Node node:curr)
                size+=node.children.size();
            List<Node> next=new ArrayList<>(size);
            for(Node node:curr){
                for(Node child:node.children)
                    next.add(child);
            }
            curr=next;
        }
        return ret;
    }
}
