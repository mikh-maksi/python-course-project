lst =[0,1,2,3,4,5,6,7,8,9,10]

def max_lst(lst):
    return max(lst)

def avg(lst):
    return sum(lst)/len(lst)

print(avg(lst))

def sum_not_null(lst):
    new_lst = []
    for elem in lst:
        if elem != 0:
            new_lst.append(elem)
    return sum(new_lst)

print(sum_not_null(lst))

def min_not_null(lst):
    new_lst = []
    for elem in lst:
        if elem != 0:
            new_lst.append(elem)
    return min(new_lst)
print(min_not_null(lst))
