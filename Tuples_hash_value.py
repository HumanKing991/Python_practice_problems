if __name__ == '__main__':
    n = int(input())
    integer_list =  [int(x) for x in input().split()]
    integer_list = tuple(integer_list)
    print(hash(integer_list))

'''Output Format

Print the result of hash(integer_list)

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''
    
