def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
arr=[1,423,45,56,12,43]
print(bubble_sort(arr))

# selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mid_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr=[1,423,45,56,12,43]
print(selection_sort(arr))

#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#merge sort
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[i])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return arr

#node definition

class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.next=None

#insert at beginning
def insert_beginning(head, value):
    new_node=ListNode(value)


# print linked list
def print_list(head):
    current=head
    while current:
        print(current.val, end=" ->")
        current=current.next
    print("None")


#insert at end
def insert_end(head,value):
    new_node=ListNode(value)
    if head is None:
        return new_node
    current=head
    while current:
        current
#insert at beginning
head=insert_beginning(head, 5)
head= insert_beginning(head, 15)
print("\n after inserting at beginning:")
print_list(head)
        

