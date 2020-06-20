/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast_ptr = head;
        ListNode* slow_ptr = head;
        
        int i = 0;
        while(fast_ptr != NULL)
        {
            fast_ptr = fast_ptr->next;
            if (i > n){
                slow_ptr = slow_ptr->next;
            }
            i++;
        }
        if (i <= n)
            head = slow_ptr->next;            
        else
            slow_ptr->next = slow_ptr->next->next;

        return head;
    }
};
