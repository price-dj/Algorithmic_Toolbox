

def merge_sort(li, c):
    if len(li) < 2: return li 
    m = len(li) // 2 
    return merge(merge_sort(li[:m],c), merge_sort(li[m:],c), c)

def merge(l, r, c):
    result = [] 
    i = j = 0 
    while i < len(l) and j < len(r): 
        if l[i] < r[j]: 
            result.append(l[i])
            i += 1 
        else: 
            result.append(r[j])
            c += (len(l) - i)
            j += 1
    result.extend(l[i:]) 
    result.extend(r[j:]) 
    return result

unsorted = [10,2,3,22,33,7,4,1,2]
(result, c) = merge_sort(unsorted, c = 0)
print(c)




