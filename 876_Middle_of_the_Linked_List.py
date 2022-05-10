# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # checked size of the Linked list
        len_list = 0
        list_ = head
        while list_ != None:
            # every time to returned loop +1
            len_list += 1
            # moved on next remaining index 
            list_ = list_.next
        
        # middle linked list  
        middle_list = len_list // 2
        
        # checkpoint of remaining index
        count = 0
        while head != None:
            # if linked list move to middle linked list return remaining linked list
            if count == middle_list:
                return head
            count += 1
            # moved on next remaining index 
            head = head.next


    class Solution:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow = fast = head
            # checked the state of the next index that reach the end of the linked list
            while fast and fast.next:
                # remaining index of linked link
                slow = slow.next
                # go to double step 
                fast = fast.next.next
            
            return slow