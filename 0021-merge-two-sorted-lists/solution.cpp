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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL)
            return l2;
        if (l2 == NULL)
            return l1;
        
        if (l1->val > l2->val)
        {
            // Ensure l1 is smaller one.
            ListNode* tmp_node = l1;
            l1 = l2;
            l2 = tmp_node;
        }
        ListNode* cur_node1 = l1;
        ListNode* cur_node2 = l2;
        
        // Loop until all two pointers reach the end.
        while(cur_node1 != NULL)
        {
            if (cur_node1->next == NULL)
            {
                cur_node1->next = cur_node2;
                break;    // break if the end of list 1 is reached.
            }
            
            if (cur_node2 == NULL)
                break;    // break if the end of list 2 is reached.  
            
            // Append l2 to l1.
            ListNode* next_node1 = cur_node1->next;
            if ((cur_node1->val <= cur_node2->val) && (next_node1->val > cur_node2->val))
            {
                cur_node1->next = cur_node2;
                
                ListNode* next_node2 = cur_node2->next;
                while ((next_node2 != NULL) && (next_node2->val < next_node1->val))
                {
                    cur_node2 = cur_node2->next;
                    next_node2 = cur_node2->next;
                }
                std::cout << cur_node2->val << next_node1->val << std::endl;
                    
                cur_node2->next = next_node1;
                
                cur_node2 = next_node2;
            }
            cur_node1 = next_node1;
            
        }
        return l1;
    }
};
