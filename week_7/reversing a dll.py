def swap(node):
    temp=node.prev
    node.prev=node.next
    node.next=temp
def reverse(llist):
    curr=llist
    prev=None
    while curr:
        swap(curr)
        prev=curr
        curr=curr.prev
    if prev:
        head=prev
    return head