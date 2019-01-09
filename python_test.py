#/usr/bin/env python
# this is my first python
# this a quick sort demo
import pdb

def quick_sort(l):
    if len(l) <= 1:
        return l
    llist, rlist = [], []
    # pdb.set_trace()
    pivot = l.pop()
    for e in l:
        if e < pivot:
            llist.append(e)
        else:
            rlist.append(e)
    return quick_sort(llist) + [pivot] + quick_sort(rlist)

if __name__ == "__main__":
    l = [3,4,1,54,76,12,6,8,1,67]
    print(quick_sort(l))