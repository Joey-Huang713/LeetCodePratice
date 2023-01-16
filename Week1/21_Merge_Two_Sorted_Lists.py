from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def linked_list(array,index=0):
    total_index = len(array)-1
    if total_index==-1:
        return None
    if index ==total_index:
        return ListNode(array[index])
    else:
        return ListNode(val=array[index],next=linked_list(array,index+1))
#自己寫的版本
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # pass
        tmp=[]
        l1=list1
        l2=list2
        while l1!=None or l2 !=None:
            if l1==None:
                tmp.append(l2.val)
                l2=l2.next
            elif l2==None:
                tmp.append(l1.val)
                l1=l1.next
            elif l1.val>=l2.val:
                tmp.append(l2.val)
                l2=l2.next
            else :
                tmp.append(l1.val)
                l1=l1.next

        return linked_list(tmp)
#參考解答後
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Result=ListNode()
        tmp=Result
        while list1 and list2:
            if list1.val>=list2.val:
                tmp.next=list2
                tmp = list2
                list2=list2.next
            else :
                tmp.next=list1
                tmp=list1
                list1=list1.next
        if list1 or list2:
            tmp.next= list1 if list1 else list2
        return Result.next
        


def show_result(l):
    while l !=None:
        print(l.val)
        l=l.next

l1 = [1,2,4]
linked_l1 = linked_list(l1)
l2 = [1,3,4]
linked_l2 = linked_list(l2)
s=Solution2()
result=s.mergeTwoLists(linked_l1,linked_l2)
show_result(result)

