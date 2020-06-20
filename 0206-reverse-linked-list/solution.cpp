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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL)
            return head;
        
        ListNode* original_head = head;
        ListNode* next_node = original_head->next;
        
        while (next_node != NULL)
        {
            // Link next node's next node to original head node.
            original_head->next = next_node->next;
            
            // Move next node to the head.
            next_node->next = head;
            
            // Set head to the moved node.
            head = next_node;
            
            // Update next_node.
            next_node = original_head->next;
        }
        return head;
    }
};
