def returnMatches(*lists):
    if not lists:
        return {"matches": [], "count": 0}
    
    common_elements = set(lists[0])
    
    for lst in lists[1:]:
        common_elements.intersection_update(lst)
    
    return {"matches": list(common_elements), "count": len(common_elements)}


if __name__ == '__main__':
    list1 = [1, 2, 3, 6]
    list2 = [3, 8, 1, 2]
    list3 = [1, 2, 4, 5]
    
    result = returnMatches(list1, list2, list3)
    
    
    print("matches:", result["matches"])
    print("count:", result["count"])
