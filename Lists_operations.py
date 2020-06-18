if __name__ == '__main__':
    N = int(input())
    x = []
    for i in range(N):
        query, *others = input().split()
        if query == 'insert':
            position,value = map(int,others)
            x.insert(position,value)
        elif query == 'print':
            print(x)
        elif query == 'remove':
            values_1 = list(map(int, others))
            x.remove(values_1[0])
        elif query == 'append':
            values_2 = list(map(int, others))
            x.append(values_2[0])
        elif query == 'pop':
            x.pop()
        elif query == 'sort':
            x.sort()
        elif query == 'reverse':
            x.reverse()


'''Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]'''
