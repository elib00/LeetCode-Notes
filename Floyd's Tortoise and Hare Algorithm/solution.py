class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def create_list():
    head = None
    curr = head
    prev = None
    
    while True:
        op = int(input("Add another node [1 - YES | 0 - NO]? "))
        if op == 1:
            val = int(input("Enter the value of the node: "))
            node = ListNode(val)
            
            prev = curr
            
            if not head:
                head = node
                curr = node
            else:
                curr.next = node
                curr = curr.next
                
        else:
            break
    
    op = int(input("Do you want to make the list into a cycle [1 - YES | 0 - NO]? "))
    if op == 1:
        if prev:
            prev.next = head
         
    return head  

def is_circular(head: ListNode) -> None:
    fast, slow = head, head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True
    
    return False
    

def print_list(head: ListNode) -> None:
    print("The elements are: ", end="")
    curr = head
    
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
        
    print()
        
        

def main():
    head = create_list()
    ans = is_circular(head)
    
    if ans: 
        print("Cycle detected")
    else:
        print("The list has no cycle")
        print_list(head)


if __name__ == "__main__":
    main()