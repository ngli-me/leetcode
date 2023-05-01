#include <iostream>
#include <stdlib.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    auto l3 = new ListNode(0);
    auto pos = l3;

    while (l1 || l2) {
        auto val1 = l1 ? l1->val : 0;
        auto val2 = l2 ? l2->val : 0;
        auto div = std::div(pos->val + val1 + val2, 10);
        pos->val = div.rem;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
        if (!l1 && !l2 && (div.quot == 0)) {
            return l3;
        }
        pos->next = new ListNode(div.quot);
        pos = pos->next;
    }
    return l3;
}

ListNode* init_list (int arr[], int size) {
    ListNode* l1 = new ListNode;
    if (size == 0) {
        l1->val = 0;
        return l1;
    } else {
        auto pos = l1;
        auto index = 0;
        while(1) {
            pos->val = arr[index];
            std::cout << "Adding " << pos->val << " ";
            index++;
            if (index < size) {
                pos->next = new ListNode;
                pos = pos->next;
            } else {
                std::cout << std::endl;
                return l1;
            }
        }
        return l1;
    }
}

void print_list (ListNode* l1) {
    while (l1->next != nullptr) {
        std::cout << l1->val << std::endl;
        l1 = l1->next;
    }
    std::cout << l1->val << std::endl;
}

int main() {
    int first_list[3] = {2,3,6}; 
    ListNode* l1 = init_list(first_list, 3);
    print_list(l1);
    auto l3 = addTwoNumbers(l1, l1);
    if (l3 != nullptr) {
        print_list(l3);
    }
    // std::cout << "Hello World!";
    return 0;
}
