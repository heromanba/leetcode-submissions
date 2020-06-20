// Definition for singly-linked list.
struct SinglyListNode {
    int val;
    SinglyListNode *next;
    SinglyListNode(int x) : val(x), next(NULL) {}
};


class MyLinkedList {
public:
    SinglyListNode* head = nullptr;
    int len = 0;
    
    /** Initialize your data structure here. */
    MyLinkedList() {
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        printList(head);
        // Invalid index;
        if ((index < 0) || (index > len - 1))
        {
            return -1;
        }
        // Current node of non-empty list.
        SinglyListNode* cur_node = head;
        for (int i = 0; i < index; i++)
        {
            cur_node = cur_node->next;
        }
        return cur_node->val;
    }
    
    /** Add a node of value val before the first element of the linked list. 
    After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        
        SinglyListNode* cur_node = new SinglyListNode(val);
        cur_node->next = head;
        head = cur_node;
        len++;    // Update length.
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        // Empty list.
        if (len == 0)
        {
            addAtHead(val);
            return;
        }
        
        // Non empty list.
        SinglyListNode* cur_node = head;
        
        while (cur_node->next != nullptr)
        {
            // Iterate over the list to find the last node.
            cur_node = cur_node->next;
        }
        
        // Create a new node.
        SinglyListNode* new_node = new SinglyListNode(val);
        
        // Current node is the last node.
        // Append the new node.
        cur_node->next = new_node;
        
        len++;    // Update length.
    }
    
    void printList(SinglyListNode* cur_node)
    {
        while (cur_node->next != nullptr)
        {
            std::cout << cur_node->val << std::endl;
            cur_node = cur_node->next;
        }
    }
    
    /** Add a node of value val before the index-th node in the linked list. 
    If index equals to the length of linked list, the node will be appended 
    to the end of linked list. If index is greater than the length, the node 
    will not be inserted. */
    void addAtIndex(int index, int val) {
        // Invalid index.
        if ((index < 0) || (index > len))
        {
            return;
        }
        // Add to first node.
        if (index == 0)
        {
            addAtHead(val);
            return;
        }
        // Non empty list.
        SinglyListNode* cur_node = head;
        for (int i = 0; i < index -1; i++)
        {
            cur_node = cur_node->next;
        }
        
        // Create a new node.
        SinglyListNode* new_node = new SinglyListNode(val);
        
        // cur_node is (index - 1)-th node.
        // Link index-th node as next of new node.
        new_node->next = cur_node->next;
        
        // Link new node as next of (index - 1)-th node.
        cur_node->next = new_node;
                
        len++;    // Update length.
        return;
        
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        // Invalid index.
        if ((index < 0) || (index > len - 1))
        {
            return;
        }
        // Delete the first node.
        if (index == 0)
        {
            head = head->next;
            len--;    // Update length.
            return;
        }
        // Non empty list and length is at least 2.
        SinglyListNode* prev_node = head;
        for (int i = 0; i < index -1; i++)
        {
            prev_node = prev_node->next;
        }
        // prev_node is (index - 1)-th node.
        // cur_node is index-th node.
        // next_node is (index + 1)-th node.
        SinglyListNode* cur_node = prev_node->next;
        SinglyListNode* next_node = cur_node->next;
        prev_node->next = next_node;
        delete cur_node;
        
        len--;    // Update length.
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
