class ListNode:
  def  __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def deleteDuplicates(self, head):

    if head == None:
      return head

    current = head.next
    prev = head
    
    while current != None:
      if current.val == prev.val:
          prev.next = current.next
          current = current.next
      else:
          current = current.next
          prev = prev.next
    
    return head

# current = 3
# prev = 1-1, 2, 3
# current.next = 
# prev.next = 1-3, 1-4, 2

# [1,1,1,1,2,3]

result1 = ListNode([1,1,2,3,3])

result = Solution()
print(result.deleteDuplicates(result1))