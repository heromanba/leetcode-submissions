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
    bool hasCycle(ListNode *head) {
        ListNode* slow_ptr = head;
        ListNode* fast_ptr = head;

        bool has_cycle = false;
        
        // Start from head.
        while (true)
        {
            // If no cycle, fast_ptr will reach the end first.
            if ((fast_ptr == NULL) || (fast_ptr->next == NULL))
            {
                break;
            }
            
            // Move two steps at a time.
            fast_ptr = fast_ptr->next->next;
            
            // Move one step at a time.
            slow_ptr = slow_ptr->next;
            
            // A cycle exists if two pointers meet.
            if (fast_ptr == slow_ptr)
            {
                has_cycle = true;
                break;
            }
        }
        return has_cycle;
        
    }
};
