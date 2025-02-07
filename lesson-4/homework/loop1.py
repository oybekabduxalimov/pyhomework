from collections import Counter

def uncommon_elements(list1, list2):
    # Count occurrences in each list
    count1, count2 = Counter(list1), Counter(list2)
    
    # Find elements unique to each list, preserving occurrences
    result = []
    for num in count1:
        if num not in count2:
            result.extend([num] * count1[num])
    for num in count2:
        if num not in count1:
            result.extend([num] * count2[num])
    
    return result