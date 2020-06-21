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
#include<cmath>

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        if (head == NULL)
            return 0;
            
        ListNode* rever_head = reverseList(head);
        ListNode* cur_node = rever_head;
        int decimal = 0;
        for (int i = 0; cur_node != NULL; i++)
        {
            decimal += cur_node->val * std::pow(2, i);
            cur_node = cur_node->next;
        }
        return decimal;
    }
    
    ListNode* reverseList(ListNode* head) {
        if (head == NULL)
            return head;
        
        ListNode* original_head = head;
        ListNode* cur_node = head->next;
        while (cur_node != NULL)
        {
            ListNode* next_node = cur_node->next;
            original_head->next = next_node;
            cur_node->next = head;
            head = cur_node;
            cur_node = next_node;
        }
        return head;
    }
};
