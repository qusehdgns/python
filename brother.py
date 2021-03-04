# class A:

#     a = 0
#     __b = 3

#     def __init__(self):
#         print('init')

# print(dir(A))

# arr = []

# for _ in range(9):
#     arr.append(int(input()))

# print(max(arr))
# print(arr.index(max(arr)))

# number = list(map(str, range(10)))

# print(number)

# s = "123456789"

# for i in s:
#     print(i)

# arr = [int(input()) for _ in range(3)]

# number = list(map(str, range(10)))

# result = str(arr[0] * arr[1] * arr[2])

# for i in number:
#     print(result.count(i))

# import numpy as np

# input_arr = [int(input()) for _ in range(10)]

# input_arr = np.array(input_arr) % 42

# input_arr = list(set(list(input_arr)))

# print(len(input_arr))

# n = int(input())

# arr = list(map(int, input().split()))

# m = max(arr[:n])

# for i, temp in enumerate(arr[:n]):
#     arr[i] = temp / m * 100

# print(sum(arr)/n)

# n = int(input())

# arr = [input() for _ in range(n)]

# for temp in arr:
#     i = 0
#     score = 0
#     for j in temp:
#         if j == 'O':
#             i += 1
#             score += i
#         elif j == 'X':
#             i = 0
    
#     print(score)

c = int(input())

arr = [list(map(int, input().split())) for _ in range(c)]

for temp in arr:
    avg = sum(temp[1:])/temp[0]
    count = 0
    for j in temp[1:]:
        if j > avg:
            count += 1
    
    print("{:.3f}%".format(count/temp[0] * 100))