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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode start = list1;
        for (int i=0; i<a-1; i++) {
            // stops at a-1 th node
            start = start.next;
        }
        ListNode end = start;
        for (int i=0; i<b-a+2; i++) {
            // stops at b+1 th node
            end = end.next;
        }
        start.next = list2;
        while (list2.next != null) 
            list2 = list2.next;
        list2.next = end;
        return list1;
    }
}
