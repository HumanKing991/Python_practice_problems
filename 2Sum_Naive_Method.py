def two_sum(lis, target):
    
    s = {}
    for i, num in enumerate(lis):
        want = target - num
        if want in s:
            return [i,s[want]]
        else:
            s[num] = i

target = int(input())
lis = [int(x) for x in input().split()]
print(two_sum(lis, target))
