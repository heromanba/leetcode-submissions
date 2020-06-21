// Definition for singly-linked list.
struct DoublyListNode {
    int val;
    DoublyListNode *next, *prev;
    DoublyListNode(int x) : val(x), next(NULL), prev(NULL) {}
};


class MyLinkedList {
public:
    DoublyListNode* head = nullptr;
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
        DoublyListNode* cur_node = head;
        for (int i = 0; i < index; i++)
        {
            cur_node = cur_node->next;
        }
        return cur_node->val;
    }
    
    /** Add a node of value val before the first element of the linked list. 
    After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        
        DoublyListNode* cur_node = new DoublyListNode(val);
        cur_node->next = head;
        if (head != NULL)
            head->prev = cur_node;
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
        DoublyListNode* cur_node = head;
        
        while (cur_node->next != nullptr)
        {
            // Iterate over the list to find the last node.
            cur_node = cur_node->next;
        }
        
        // Create a new node.
        DoublyListNode* new_node = new DoublyListNode(val);
        
        // Current node is the last node.
        // Append the new node.
        cur_node->next = new_node;
        new_node->prev = cur_node;
        len++;    // Update length.
    }
    
    void printList(DoublyListNode* cur_node)
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
        if (index == len)
        {
            addAtTail(val);
            return;
        }
        // Non empty list.
        DoublyListNode* cur_node = head;
        for (int i = 0; i < index; i++)
        {
            cur_node = cur_node->next;
        }
        
        // Create a new node.
        DoublyListNode* new_node = new DoublyListNode(val);
        
        // prev_node is (index - 1)-th node.
        // cur_node is index-th node.
        // next_node is (index + 1)-th node.
        DoublyListNode* prev_node = cur_node->prev;
        DoublyListNode* next_node = cur_node->next;
        
        // Link index-th node as next of new node.
        new_node->next = cur_node;
        new_node->prev = prev_node;
        
        cur_node->prev = new_node;
        prev_node->next = new_node;
                
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
        DoublyListNode* cur_node = head;
        for (int i = 0; i < index; i++)
        {
            cur_node = cur_node->next;
        }
        // prev_node is (index - 1)-th node.
        // cur_node is index-th node.
        // next_node is (index + 1)-th node.
        DoublyListNode* prev_node = cur_node->prev;
        DoublyListNode* next_node = cur_node->next;
        if (prev_node != NULL)
            prev_node->next = next_node;
        if (next_node != NULL)
            next_node->prev = prev_node;
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
