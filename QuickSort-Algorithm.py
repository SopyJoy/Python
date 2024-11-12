def partition(start,end,lst):
    indexP = start
    pivot = lst[indexP]

    while start < end:
        while start < len(lst) and lst[start] <= pivot:
            start +=1
        while lst[end] > pivot:
            end-=1
        if start < end:
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
    temp = lst[indexP]
    lst[indexP] = lst[end]
    lst[end] = temp
    return end

def first(start, end , lst):
    if start < end:
        part = partition(start, end, lst)
        first(start,part-1,lst)
        first(part+1,end,lst)

lst = [25,63,45,78,30,96,15,60]
print("Sofia Joy D. Yunun")
print("Square")
print("Algorithm: Quick Sort-First Element Order: Ascending")
print("Given Elements: 25,63,45,78,30,96,15,60")
first(0,len(lst)-1,lst)
print("Order", lst)
