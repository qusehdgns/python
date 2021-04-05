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

# c = int(input())

# arr = [list(map(int, input().split())) for _ in range(c)]

# for temp in arr:
#     avg = sum(temp[1:])/temp[0]
#     count = 0
#     for j in temp[1:]:
#         if j > avg:
#             count += 1
    
#     print("{:.3f}%".format(count/temp[0] * 100))

# def delete_calc(max_num):
#     request_list = list(range(1, max_num + 1))

#     for temp in list(range(1, max_num + 1)):
#         calc = temp
#         for i in str(temp):
#             calc += int(i)
        
#         if calc in request_list:
#             request_list.remove(calc)

#     return request_list


# for i in delete_calc(10000):
#     print(i)

# def count_calc(max_num):
#     result = set()
#     for i in range(1, 10):
#         for j in range(-i, (10-i)):
#             input_num = i
#             while input_num <= max_num:
#                 result.add(input_num)
#                 temp = (input_num % 10) + j
#                 if temp < 0 or temp >= 10:
#                     break
#                 else:
#                     input_num = input_num * 10 + temp

#     return len(result)

# print(count_calc(int(input())))

# print(ord(input()))

# n = int(input())
# str = input()
# result = 0

# for i in str[:n]:
#     result += int(i)

# print(result)

# string = input()
# result = []

# for i in range(ord('a'), ord('z')+1):
#     result.append(string.find(chr(i)))

# for temp in result:
#     print(temp, end=' ')

# n = int(input())
# result = []

# for _ in range(n):
#     num, string = input().split()
#     num = int(num)

#     temp_result = ""
#     for i in string:
#         temp_result += i * num

#     result.append(temp_result)

# for temp in result:
#     print(temp)

# string = input().upper()
# most = ['', 0]

# for n in range(ord('A'), ord('Z') + 1):
#     if string.count(chr(n)) > most[1]:
#         most[0] = chr(n)
#         most[1] = string.count(chr(n))
#     elif string.count(chr(n)) == most[1]:
#         most[0] = '?'

# print(most[0])

# print(len(input().split()))

# first, second = map(reversed, input().split())

# arr = input().split()

# for i in range(len(arr)):
#     arr[i] = arr[i][::-1]

# print(max(arr))

# string = input()
# time = 0

# for spell in string:
#     if ord(spell) in list(range(ord('A'), ord('D'))):
#         time += 3
#     elif ord(spell) in list(range(ord('D'), ord('G'))):
#         time += 4
#     elif ord(spell) in list(range(ord('G'), ord('J'))):
#         time += 5
#     elif ord(spell) in list(range(ord('J'), ord('M'))):
#         time += 6
#     elif ord(spell) in list(range(ord('M'), ord('P'))):
#         time += 7
#     elif ord(spell) in list(range(ord('P'), ord('T'))):
#         time += 8
#     elif ord(spell) in list(range(ord('T'), ord('W'))):
#         time += 9
#     elif ord(spell) in list(range(ord('W'), ord('Z') + 1)):
#         time += 10

# print(time)

# string = input()

# alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# for temp in alpa:
#     if temp in string:
#         string = string.replace(temp, " ")

# print(len(string))

# n = int(input())

# strings = [input() for _ in range(n)]
# result = []

# for string in strings:
#     if len(string) > 1:
#         check = True
#         for i in range(len(string)-1):
#             if string[i] != string[i+1] and string[i] in string[i+1:]:
#                 check = False
#                 break
        
#         if check:
#             result.append(string)
#     else:
#         result.append(string)

# print(len(result))

# a = range(10)

# print(list(a))

# arr = ['1', '2', '3']

# print(str(eval('*'.join(arr))))

# result = list(range(1,10001))

# def solve(num):
#     global result
#     num = num+sum([int(i) for i in str(num)])
#     if num<=10000 and num in result:
#         result.remove(num)
#         return solve(num)
#     else:
#         return 0

# for i in result:
#     solve(i)
#     print(i)

# S = input()
# [print(S.find(chr(i)), end=' ') for i in range(ord('a'), ord('z')+1, 1)]


# for j in range(5):
#     print(j)
#     if j == 3:
#         pass
# else:
#     print("else", j)

# string = ".....TWwde%@#!$"

# print(string.lower())

<<<<<<< Updated upstream
# def calc(num):

#     num_check = num

#     count = 0
#     result = []

#     for i in range(1,num+1):
        
#         if num_check - i <= 0:
#             count = i
#             break
        
#         num_check -= i
        

#     print(count)
#     if count % 2 == 0:
#         result = [1, count]
#         for _ in range(1, num_check):
#             result[0] += 1
#             result[1] -= 1
#     else:
#         result = [count, 1]
#         for _ in range(1, num_check):
#             result[1] += 1
#             result[0] -= 1

#     return result

# num = int(input())

# result = calc(num)

# print(f"{result[0]}/{result[1]}")

# N = int(input())
# case = list(map(int,input().split()))
# result = 0

# for temp in case[:N]:
#     if temp > 1:
#         check = True
#         for i in range(2, temp):
#             if temp % i == 0:
#                 check = False
#                 break
        
#         if check:
#             result += 1

# print(result)

# M = int(input())
# N = int(input())

# result = []

# for temp in range(M, N+1):
#     if temp > 1:
#         check = True
#         for i in range(2, temp):
#             if temp % i == 0:
#                 check = False
#                 break
        
#         if check:
#             result.append(temp)

# if len(result) > 0:
#     print(sum(result))
#     print(result[0])
# else:
#     print(-1)

# N = int(input())

# while N != 1:
#     for i in range(2, N+1):
#         if N % i == 0:
#             print(i)
#             N //= i
#             break

# M, N = map(int, input().split())

# result = list(range(M, N+1))

# if 1 in result:
#     result.remove(1)

# for temp in range(2, result[-1]):
#     i = 2
#     j = temp
#     while i * j <= N:
#         if (i * j) in result:
#             result.remove(i * j)
        
#         i += 1

# for temp in result:
#     check = True
#     for i in range(2, temp):
#         if temp % i == 0:
#             check = False
#             break
#     if check:
#         print(temp)

# while True:
#     n = int(input())

#     if n == 0:
#         break

#     count = 0
#     for temp in range(n+1, (2*n)+1):
#         if temp > 1:
#             check = True
#             for i in range(2, temp):
#                 if temp % i == 0:
#                     check = False
#                     break
            
#             if check:
#                 count += 1

#     print(count)

# x, y, w, h = map(int, input().split())

# result = [x, y, w-x, h-y]

# print(min(result))

# xs = []
# ys = []

# for _ in range(3):
#     x, y = map(int, input().split())
#     if x in xs:
#         xs.remove(x)
#     else:
#         xs.append(x)
    
#     if y in ys:
#         ys.remove(y)
#     else:
#         ys.append(y)

# print(xs[0], ys[0])

# while True:
#     temp = list(map(int, input().split()))

#     temp.sort()

#     if temp.count(0) == 3:
#         break

#     if (temp[0]**2) + (temp[1]**2) == (temp[-1]**2):
#         print("right")
#     else:
#         print("wrong")

# T = int(input())

# for _ in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())

#     r = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)

#     if r == 0 and r1 == r2:
#         print(-1)
#     elif r1 + r2 == r or r2 + r == r1 or r1 + r == r2:
#         print(1)
#     elif r1 + r2 < r or r2 + r < r1 or r1 + r < r2:
#         print(0)
#     else:
#         print(2)

# import math

# r = int(input())

# print("{:.6f}".format((r ** 2) * math.pi))
# print("{:.6f}".format((r ** 2) * 2))

# m, n = map(int,input().split())

# for i in range(m, n+1):
#     if i > 1:
#         check = True
#         j = 2
#         while j * j <= i:
#             if i % j == 0:
#                 check = False
#                 break
#             i += 1
        
#         if check:
#             print(i)

# def solution(n, arr1, arr2):
#     cal = [2 ** i for i in range(n)][::-1]
    
#     map1 = []
#     map2 = []
    
#     for temp in arr1:
#         temp_list = []
#         for i in range(len(cal)):
#             if temp >= cal[i]:
#                 temp -= cal[i]
#                 temp_list.append(1)
#             else:
#                 temp_list.append(0)
#         map1.append(temp_list)
        
#     for temp in arr2:
#         temp_list = []
#         for i in range(len(cal)):
#             if temp >= cal[i]:
#                 temp -= cal[i]
#                 temp_list.append(1)
#             else:
#                 temp_list.append(0)
#         map2.append(temp_list)
        
#     map = [[0] * n for _ in range(n)]
        
#     for i in range(len(map)):
#         for j in range(len(map[0])):
#             if map1[i][j] == 1 or map2[i][j] == 1:
#                 map[i][j] = '#'
#             else:
#                 map[i][j] = ' '
                
#         map[i] = ''.join(map[i])

#     return map


# print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))

# def solution(scoville, K):
#     count = 0
    
#     while min(scoville) < K:
#         count += 1
#         first = scoville.pop(0)
#         second = scoville.pop(0)
    
#         if first + (second * 2) >= K:
#             scoville.append(first + (second * 2))
#         else:
#             for i in range(len(scoville)):
#                 if first + (second * 2) < scoville[i]:
#                     scoville.insert(i, first + (second * 2))
        
#     return count

# print(solution([1,2,3,9,10,12], 7))

test = "--2-342afAFADFADF"
test.lower()

print(test.lower())
=======

N = int(input())
S = (3, 5)

for i in range(0, N+1, S[0]):
    if (N-i)%S[1]==0:
        print(((N-i)//S[1]) + i//S[0])
        break
else:
    print(-1)
>>>>>>> Stashed changes
