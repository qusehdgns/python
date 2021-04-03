# def solution(board, moves):
#     result = []
    
#     for value in moves:
#         for floor in board:
#             if floor[value-1] != 0:
#                 catch = floor[value-1]
#                 floor[value-1] = 0
#                 if len(result) != 0:
#                     if result[-1] == catch:
#                         result.pop()
#                     else:
#                         result.append(catch)
#                 else:
#                     result.append(catch)
                
                
#                 print(result)
#                 break
#         print(board)
    
#     answer = len(result)

#     return answer

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]

# print(board)
# print(solution(board, moves))

# d = []
# print(sum(d))

# def solution(bridge_length, weight, truck_weights):
    
#     on_bridge = []
#     on_bridge_time = []
    
#     time = 0
    
#     while len(truck_weights) != 0 or len(on_bridge) != 0:
#         if len(on_bridge) > 0:
#             if time - on_bridge_time[0] == bridge_length:
#                 on_bridge.pop(0)
#                 on_bridge_time.pop(0)

#         if len(truck_weights) > 0:
#             if sum(on_bridge) + truck_weights[0] <= weight:
#                 on_bridge_time.append(time)
#                 on_bridge.append(truck_weights.pop(0))
            
#         time += 1
        
#     return time

# print(solution(2,10,[7,4,5,6]))

# def solution(expression):
    
#     op_pa = ['+', '-', '*']
#     str_list = []

#     start_pos = 0

#     for i in range(len(expression)):
#         if expression[i] not in op_pa and start_pos >= i:
#             start_pos = i

#         if expression[i] in op_pa:
#             str_list.append(expression[start_pos:i])
#             str_list.append(expression[i])
#             start_pos = i + 1
        
#         if i == len(expression) - 1:
#             str_list.append(expression[start_pos:])

#     calc_pa = [[0,1,2], [1,0,2], [1,2,0], [2,0,1], [2,1,0], [0,2,1]]

#     result = []

#     for temp in calc_pa:
#         calc_str = str_list[:]
#         for pat in temp:
#             while calc_str.count(op_pa[pat]) != 0:
#                 i = 0
#                 while i < len(calc_str):
#                     if calc_str[i] == op_pa[pat]:
#                         last = calc_str.pop(i+1)
#                         op = calc_str.pop(i)
#                         first = calc_str.pop(i-1)
#                         calc = eval(first+op+last)
#                         calc_str.insert(i-1, str(calc))
#                         break

#                     i += 1
            
#         result.append(abs(int(calc_str[0])))

#     return max(result)

# def solution(clothes):
#     part = []
#     for temp in clothes:
#         part.append(temp[1])
    
#     part_sec = set(part)
    
#     part_count = []
    
#     for temp in part_sec:
#         part_count.append(part.count(temp))
    
#     pos = 1
    
#     for temp in part_count:
#         pos *= temp + 1
    
#     pos -= 1
    
#     return pos
        

# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))


# 망가진 코드
# def solution(routes):
#     same_root = []
    
#     for temp in routes:
#         if len(same_root) < 1:
#             same_root.append(temp)
#         else:
#             check = True
#             for part in same_root:
#                 start_check = False
#                 print(list(range(part[0], part[1] + 1)))
#                 for i in range(temp[0], temp[1] + 1):
#                     if i in range(part[0], part[1]+1) and start_check == False:
#                         print(i)
#                         part[0] = i
#                         start_check = True
#                     elif i not in range(part[0], part[1]+1) and start_check == True:
#                         print(i)
#                         part[1] = i-1
#                         check = False
#                         start_check = False
#                         print()
#                         break                        
            
#             print(check)
#             if check:
#                 print(temp)
#                 same_root.append(temp)
    
#     answer = len(same_root)
                
#     return same_root

# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))

# def solution(n):
#     n = n - 1
#     nums = ["1", "2", "4"]
#     i = 0
#     if n != 0:
#         while 3 ** i <= n:
#             i += 1
#     else:
#         i = 1
        
#     result = []
    
#     tri = [3 ** i for i in range(i)]
    
#     for temp in tri[::-1]:
#         result.append(n // temp)
#         n %= temp
    
#     answer = int(''.join([nums[i] for i in result]))
    
#     return answer

# print(solution(1))

# def solution(n):
#     answer = bin(n)[2:][::-1]
    
#     point = answer.index('1')
    
#     answer = answer[point+1:][::-1]
    
#     answer = "0b10" + answer
    
#     return int(answer, 2)

# print(solution(2))

# def solution(s):
#     i = 0
#     while i < len(s) - 1:
#         if s[i] == s[i+1]:
#             s = s.replace(s[i]+s[i], "")
#             i = 0
            
#             if len(s) == 0:
#                 return 1
#         else:
#             i += 1

#     return 0

# print(solution("sssbsb"))

# from itertools import permutations

# def solution(numbers, K):
    
#     arr = list(permutations(numbers))
            
#     print(arr)
    
#     return

# solution([10, 40, 30, 20], 20)

# from itertools import permutations
# import math

# def solution(numbers, K):
    
#     arr = list(permutations(numbers))
               
#     result = len(numbers)
               
#     for temp in arr:
#         for i in range(1, len(temp)-1):
#             if abs(temp[i] - temp[i-1]) > K or abs(temp[i]-temp[i+1]) > K:
#                 break
#         else:
#             count = 0
#             for i in range(len(temp)):
#                 if temp[i] != numbers[i]:
#                     count += 1
            
#             if math.ceil(count / 2) < result:
#                 result = math.ceil(count / 2)

#     return result

# print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))

# def solution(grid, K):
#     result = []
#     for i in range(len(grid) - (K - 1)):
#         temp = []
#         for j in range(len(grid) - (K - 1)):
#             calc = 0
#             for z in range(K):
#                 for x in range(K):
#                     calc += grid[i+z][j+x]
            
#             temp.append(calc)
        
#         result.append(temp)
    
#     calc_result = []
#     for i in range(len(result) - K): 
#         for j in range(len(result)):
#             a = result[i][j]
#             for x in range(i, i + K):
#                 for y in range(j + K, len(result)):
#                     calc_result.append(a + result[x][y])
            
#             for x in range(i + K, len(result)): 
#                 for y in range(len(result)):
#                     calc_result.append(a + result[x][y])
    
#     return max(calc_result)

# print(solution([[3, 4, 5], [2, 3, 4], [1, 2, 3]], 1))
# print(solution([[2, 1, 1, 0, 1], [1, 2, 0, 3, 0], [0, 1, 5, 1, 2], [0, 0, 1, 3, 1], [1, 2, 0, 1, 1]], 2))

# def solution(rows, columns, queries):
#     case = [[temp + 1 for temp in range((i*columns), ((i+1) * columns))] for i in range(rows)]

#     result = []

#     for query in queries:
#         min = rows * columns
#         temp1 = case[query[0]-1][query[1]-1]
#         temp2 = 0

#         for j in range(query[1], query[3]):
#             temp2 = case[query[0] - 1][j]
#             case[query[0] - 1][j] = temp1
#             temp1 = temp2
#             if temp1 < min:
#                 min = temp1

#         for i in range(query[0], query[2]):
#             temp2 = case[i][query[3] - 1]
#             case[i][query[3] - 1] = temp1
#             temp1 = temp2
#             if temp1 < min:
#                 min = temp1

#         for j in range(query[3] - 2, query[1] - 2, -1):
#             temp2 = case[query[2] - 1][j]
#             case[query[2] - 1][j] = temp1
#             temp1 = temp2
#             if temp1 < min:
#                 min = temp1

#         for i in range(query[2] - 2, query[0] - 2, -1):
#             temp2 = case[i][query[1] - 1]
#             case[i][query[1] - 1] = temp1
#             temp1 = temp2
#             if temp1 < min:
#                 min = temp1
            
#         result.append(min)  

#     return result

# print(solution(100, 97, [[1,1,100,97]]))


# def solution(enroll, referral, seller, amount):
    
#     money_dict = dict()
    
#     for name in enroll:
#         money_dict[name] = 0
    
#     for who, count in zip(seller, amount):
#         cost = count * 100
#         name = who
#         while name != "-":
#             money_dict[name] += round(cost * 0.9)
#             cost = round(cost * 0.1)
#             name = referral[enroll.index(name)]
        
#     return list(money_dict.values())
        
#     return money_dict

# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], 
# ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], 
# ["sam", "emily"], [2, 3]))


 
# from itertools import product

# def solution(n, p, c):
#     base_arr = [i for i in range(n)]
    
#     arr = [base_arr for _ in range(c)]
    
#     arr = [sum([i ** p for i in temp]) % n for temp in product(*arr)]
    
#     result = []
#     for i in base_arr:
#         result.append(arr.count(i))
    
#     return result