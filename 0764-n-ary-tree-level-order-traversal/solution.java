

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ret = new LinkedList<>();
        if (root==null)
            return ret;
        Queue<Node> curr=new LinkedList<>();
        curr.add(root);
        while(!curr.isEmpty()) {
            Queue<Node> next=new LinkedList<>();
            List<Integer> tmpList=new ArrayList<>();
            while(!curr.isEmpty()) {
                Node tmp=curr.poll();
                tmpList.add(tmp.val);
                for(Node n:tmp.children)
                    next.add(n);
            }
            if(!tmpList.isEmpty())
                ret.add(tmpList);
            curr=next;
        }
        return ret;
    }
}
