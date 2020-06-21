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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL)
            return l2;
        if (l2 == NULL)
            return l1;
        
        ListNode* cur_node1 = l1;
        ListNode* cur_node2 = l2;
        
        ListNode* sum_head = new ListNode();
        ListNode* sum_node = sum_head;
        
        bool increment = false;
        int cur_node1_val = 0;
        int cur_node2_val = 0;
        for (int i = 0; true; i++)
        {
            if ((cur_node1 == NULL) && (cur_node2 == NULL))
            {
                if (increment)
                    sum_node->next = new ListNode(1);
                break;
            }
            
            if (i > 0)
            {
                sum_node->next = new ListNode();
                sum_node = sum_node->next;
            }
            
            if (cur_node1 == NULL)
                cur_node1_val = 0;
            else
                cur_node1_val = cur_node1->val;
                
            if (cur_node2 == NULL)
                cur_node2_val = 0;
            else
                cur_node2_val = cur_node2->val;
            
            // Add two numbers in the same digit.
            sum_node->val = cur_node1_val + cur_node2_val;
            
            if (increment)
            {
                sum_node->val += 1;
                increment = false;
            }
            
            // If sum is larger than 10 increment next digit by 1.
            if (sum_node->val >= 10)
            {
                sum_node->val %= 10;
                increment = true;
            }
                        
            if (cur_node1 != NULL)
                cur_node1 = cur_node1->next;
            
            if (cur_node2 != NULL)
                cur_node2 = cur_node2->next;
        }
        return sum_head;
    }
};
