# Complete the getSequenceSum function below.
def getSequenceSum(i, j, k):
    # total_sum = sum(range(i, j+1)) + sum(reversed(range(k, j))) # not ideal solution
    
    # more ideal solution: if start to mid overlaps with mid to end, then use it again
    total_sum = sum(range(i, j+1))  # add from start to mid inclusive
    
    if k == i:
        total_sum = ((total_sum - j) * 2) + j
    elif k < i:
        total_sum = ((total_sum - j) * 2) + j + sum(reversed(range(k, i)))
    else:
        total_sum += sum(reversed(range(k, j)))
    return total_sum