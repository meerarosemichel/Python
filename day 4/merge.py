#merge two sorted lists
def merge_two_lists(list1, list2):
    combined = list1 + list2
    combined.sort()
    
    return combined
l1 = [1, 2, 4]
l2 = [1, 3, 4]

result = merge_two_lists(l1, l2)
print(result)  
