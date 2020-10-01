def bsearch(list, idx0, idxn, val):

    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
# Compare the search item with middle most value

        if list[midval] > val:
            return bsearch(list, idx0, midval-1,val)
        elif list[midval] < val:
            return bsearch(list, midval+1, idxn, val)
        else:
            return midval

list = [2,7,19,34,53,72]
print(bsearch(list, 0, 5, 19))
print(bsearch(list, 0, 5, 11))