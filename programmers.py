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
def solution(routes):
    same_root = []
    
    for temp in routes:
        if len(same_root) < 1:
            same_root.append(temp)
        else:
            check = True
            for part in same_root:
                start_check = False
                print(list(range(part[0], part[1] + 1)))
                for i in range(temp[0], temp[1] + 1):
                    if i in range(part[0], part[1]+1) and start_check == False:
                        print(i)
                        part[0] = i
                        start_check = True
                    elif i not in range(part[0], part[1]+1) and start_check == True:
                        print(i)
                        part[1] = i-1
                        check = False
                        start_check = False
                        print()
                        break                        
            
            print(check)
            if check:
                print(temp)
                same_root.append(temp)
    
    answer = len(same_root)
                
    return same_root

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))