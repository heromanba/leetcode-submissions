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
    bool isPalindrome(ListNode* head) {
        if (head == NULL)
            return true;
        
        // Copy list with reversed order.
        ListNode* rever_head = copyReversedList(head);
        
        ListNode* cur_node = head->next;
        ListNode* rever_cur_node = rever_head->next;
        
        while ((rever_cur_node != NULL) && (cur_node != NULL))
        {
            // std::cout << rever_cur_node->val << cur_node->val << endl;
            if (rever_cur_node->val != cur_node->val)
                return false;
            cur_node = cur_node->next;
            rever_cur_node = rever_cur_node->next;
        }
        return true;
    }
    
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
    
    ListNode* copyReversedList(ListNode* head) {
        if (head == NULL)
            return head;
        
        ListNode* rever_cur_node = new ListNode(head->val);
        
        ListNode* cur_node = head->next;
        while (cur_node != NULL)
        {
            // std::cout << rever_cur_node->val << std::endl;
            // Temporary variable to reverse the list.
            ListNode* rever_prev_node = new ListNode();
            rever_prev_node->val = cur_node->val;
            rever_prev_node->next = rever_cur_node;
            
            // Move pointer forward.
            rever_cur_node = rever_prev_node;
            
            cur_node = cur_node->next;
        }
        printList(rever_cur_node);
        return rever_cur_node;
    }
    
    void printList(ListNode* cur_node)
    {
        // std::cout << (cur_node == NULL) << std::endl;
        while (cur_node != NULL)
        {
            std::cout << cur_node->val << std::endl;
            cur_node = cur_node->next;
        }
    }
};
