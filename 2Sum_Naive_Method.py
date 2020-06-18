def two_sum(lis, target):
    
    for i in lis:
        for j in range(1, len(lis)):
            if i + lis[j] == target:
                return [lis.index(i),j]
    return "Target Sum not found "

target = int(input())
lis = [int(x) for x in input().split()]
print(two_sum(lis, target))
                
            
