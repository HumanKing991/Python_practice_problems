def search_insert_position(lis,n):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low + high) // 2
        if lis[mid] == n:
            return mid
        elif n > lis[mid] :
            low = mid + 1
        else:
            high = mid - 1
    return low

n = int(input('Enter your Target Integer : '))
lis = [int(x) for x in input().split()]
print(search_insert_position(lis, n))
    
