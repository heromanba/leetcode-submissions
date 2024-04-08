/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        int i=1;
        ListNode src=head;
        while(i<k){
            src=src.next;
            i++;
        }
        ListNode slow=head;
        ListNode fast=head;
        int j=1;
        while(fast.next!=null){
            if(j>=k)
                slow=slow.next;
            fast=fast.next;
            j++;
        }
        int tmp=src.val;
        src.val=slow.val;
        slow.val=tmp;
        return head;
    }
}
