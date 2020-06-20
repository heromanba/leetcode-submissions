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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // a * c b * c
        ListNode* ptr1 = headA;
        bool ptr1_changed = false;
        
        // b * c a * c
        ListNode* ptr2 = headB;
        bool ptr2_changed = false;
        
        while(ptr1 != ptr2)
        {
            if ((ptr1 == NULL) && (!ptr1_changed))
            {
                ptr1 = headB;
                ptr1_changed = true;
            }
            else
                ptr1 = ptr1->next;
                
            if ((ptr2 == NULL) && (!ptr2_changed))
            {
                ptr2 = headA;
                ptr2_changed = true;
            }
            else
                ptr2 = ptr2->next;
        }
        return ptr1;
    }
};
