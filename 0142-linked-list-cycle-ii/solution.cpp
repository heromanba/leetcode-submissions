/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow_ptr = head;
        ListNode* fast_ptr = head;
        ListNode* intersect = NULL;
        
        // Start from head.
        while (true)
        {
            // If no cycle, fast_ptr will reach the end first.
            if ((fast_ptr == NULL) || (fast_ptr->next == NULL))
            {
                return NULL;
            }
            
            // Move two steps at a time.
            fast_ptr = fast_ptr->next->next;
            
            // Move one step at a time.
            slow_ptr = slow_ptr->next;
            
            // A cycle exists if two pointers meet.
            if (fast_ptr == slow_ptr)
            {
                intersect = slow_ptr;
                break;
            }
        }
        
        ListNode* ptr1 = head;
        ListNode* ptr2 = intersect;
        while (ptr1 != ptr2){
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        return ptr1;
    }
};
