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
    void printList(ListNode* cur_node)
    {
        while (cur_node->next != nullptr)
        {
            std::cout << cur_node->val;
            cur_node = cur_node->next;
        }
    }
    
    ListNode* oddEvenList(ListNode* head) {
        if (head == NULL)
            return head;
        
        // Get current position.
        ListNode* ptr1 = head;
        
        // Get all odds nodes.
        ListNode* ptr2 = head;
        ptr2 = ptr2->next;
        
        // Run this only list has at least 3 nodes.
        while ((ptr2 != NULL) && (ptr2->next != NULL))
        {
            ListNode* tmp_node = ptr2->next;
                        
            ptr2->next = ptr2->next->next;
            
            tmp_node->next = ptr1->next;
            ptr1->next = tmp_node;
            
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        return head;
    }
};
