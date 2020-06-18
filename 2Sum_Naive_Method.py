def two_sum(lis, target):
    
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i]+ lis[j] == target:
                return [i,j]
    return "Target Sum not found "

target = int(input())
lis = [int(x) for x in input().split()]
print(two_sum(lis, target))
