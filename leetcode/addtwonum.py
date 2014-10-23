# Definition for singly-linked list.
#ListNode val,next

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        
def addTwoNumbers(self,l1, l2):
        head=ListNode(0)
        p=head
        flag=0
        while(l1 and l2):
            a=l1.val+l2.val+flag
            if(a>=10):
                a=a-10
                flag=1
            else:
                flag=0
            l1=l1.next
            l2=l2.next
            tmp=ListNode(a)
            p.next=tmp
            p=p.next
        while(l1):
            a=l1.val+flag
            if(a>=10):
                a=a-10
                flag=1
            else:
                flag=0
            l1=l1.next
            tmp=ListNode(a)
            p.next=tmp
            p=p.next
        while(l2):
            a=l2.val+flag
            if(a>=10):
                a=a-10
                flag=1
            else:
                flag=0
            l2=l2.next
            tmp=ListNode(a)
            p.next=tmp
            p=p.next
        if(flag==1):
            tmp=ListNode(1)
            p.next=tmp
            p=p.next
        return head.next
