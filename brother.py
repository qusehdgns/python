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

result = list(range(1,10001))

def solve(num):
    global result
    num = num+sum([int(i) for i in str(num)])
    if num<=10000 and num in result:
        result.remove(num)
        return solve(num)
    else:
        return 0

for i in result:
    solve(i)
    print(i)