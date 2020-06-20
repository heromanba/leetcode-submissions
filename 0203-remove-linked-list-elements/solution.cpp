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
    ListNode* removeElements(ListNode* head, int val) {
        if (head == NULL)
            return head;
        
        // Ensure head is safe.
        while ((head != NULL) && (head->val == val))
            head = head->next;
        
        ListNode* prev_node = head;
        // Normal case.
        while (prev_node != NULL)
        {
            ListNode* cur_node = prev_node->next;
            
            while ((cur_node != NULL) && (cur_node->val == val))
            {
                ListNode* next_node = cur_node->next;
                prev_node->next = next_node;
                cur_node = prev_node->next;
            }
            prev_node = prev_node->next;
        }
        return head;
    }
};
