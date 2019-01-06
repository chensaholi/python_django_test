#/usr/bin/env python
# this is my first python
# this a quick sort demo
import pdb

def quick_sort(l):
    if len(l) <= 1:
        return l
    llist, rlist = [], []
    flag = l[int(len(l)/2)]
    # pdb.set_trace()
    for e in l:
        if e < flag:
            llist.append(e)
        else:
            rlist.append(e)
    print(llist, rlist)
    return quick_sort(llist) + quick_sort(rlist)

if __name__ == "__main__":
    l = [3,4,1,54,76,12,6,8,1,67]
    quick_sort(l)