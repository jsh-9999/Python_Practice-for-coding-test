# import sys
#
# data = sys.stdin.readline().rstrip()
# print(data)
# answer =7

# print(f"정답은 {answer}입니다")

# result = eval("(3+5)*2")

# print(result)

# result = sorted([9,1,8,5,4])
# print(result)   오름차순으로 정렬
#
# result = sorted([9,1,8,5,4],reverse=True)
# print(result)  내림차순으로 정렬

# from itertools import permutations  순서를 고려하는 순열
#
# data = ['A', 'B', 'C']
#
# result = list(permutations(data, 3))
#
# print(result)

# from itertools import combinations 순서를 고려치 않는 조합
#
# data = ['A', 'B', 'C']
#
# result = list(combinations(data, 2))
#
# print(result)

# from itertools import product  순서를 고려하되 원소의 중복을 허용하고 뽑고자 하는 데이터의 수를 정할 수 있는 순열
#
# data = ['A', 'B', 'C']
# result = list(product(data, repeat=2))
# print(result)


# from itertools import combinations_with_replacement  순서를 고려치 않고 원소의 중복을 허용하고 뽑고자 하는 데이터의 수를 정할 수 있는 조합
#
# data = ['A', 'B', 'C']
# result = list(combinations_with_replacement(data,2))
# print(result)

import heapq

# def heapsort(iterable):
#     h=[]
#     result =[]
#     for value in iterable:
#         heapq.heappush(h, value)
#     for _ in range(len(h)):
#         result.append(heapq.heappop(h))
#
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,9])
# print(result)


# from bisect import bisect_left,bisect_right
# a=[1,2,4,4,4,8]
# x=10
# print(bisect_left(a,x))
# print(bisect_right(a,x))

# from bisect import bisect_left, bisect_right
#
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a,right_value)
#     left_index= bisect_left(a,left_value)
#     return right_index - left_index
#
#
# a=[1,2,3,3,3,3,4,4,8,9]
#
#
# print(count_by_range(a,4,4))
# print(count_by_range(a,-1,3))

# n = int(input())
#
# data = list(map(int, input().split()))  list()로 다시 바꾼음로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장
#
# data.sort(reverse=True)  내림차순으로 정렬
#
# print(data)

# n,m,k=map(int,input().split())
#
# print(n,m,k)

