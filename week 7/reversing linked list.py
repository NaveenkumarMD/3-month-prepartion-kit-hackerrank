def reverse(head):
    curr=head
    prev,nex=None,None
    while curr:
        nex=curr.next
        curr.next=prev
        prev=curr
        curr=nex
    return prev