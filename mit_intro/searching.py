def linearSearch(L, e):
    found = False
    i = 0
    ctr = 0
    while i<len(L) and found == False:
        ctr += 1
        if e == L[i]:
            found = True
        i += 1
    print (found, ctr)

def bSearch(L, e, first, last, calls):
    print (first, last, calls)
    if (last-first)<2:
        return L[first]==e or L[last]==e
    mid = int(first + (last-first)/2)
    if L[mid]==e:
        return True
    if L[mid]>e:
        return bSearch(L, e, first, mid-1, calls+1)
    return bSearch(L, e, mid+1, last, calls+1)

def search(L, e):
    print("Linear search")
    linearSearch(L, e)
    print("Binary search")
    print (bSearch(L, e, 0, len(L)-1, 1))

L1=[1, 2, 3, 4, 6, 8, 10, 12, 16, 80]
e1=12
L2=[198, 430, 600, 19877, 176655]
e2= 7777
search(L1, e1)
search(L2, e2)
