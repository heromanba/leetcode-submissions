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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null) {
            // calculate the gcd value
            int a = Math.max(slow.val, fast.val);
            int b = Math.min(slow.val, fast.val);
            int gcdVal = gcd(a, b);
            // insert the node with gcd value
            ListNode gcdNode = new ListNode(gcdVal, fast);
            slow.next = gcdNode;
            slow = fast;
            fast = fast.next;
        }
        return head;
    }

    public int gcd(int a, int b) {
        // function gcd(a, b)
        // while b ≠ 0
        //     t := b
        //     b := a mod b
        //     a := t
        // return a
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}
