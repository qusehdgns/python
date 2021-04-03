# 카카오커머스 1번

# from itertools import product

# def solution(n, p, c):
#     base_arr = [i for i in range(n)]
    
#     arr = [base_arr for _ in range(c)]
    
#     arr = [sum([i ** p for i in temp]) % n for temp in product(*arr)]
    
#     result = []
#     for i in base_arr:
#         result.append(arr.count(i))
    
#     return result

# 카카오커머스 2번

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

# def calc(grid, x, y, K):
#     s = 0
#     for i in range(K):
#         for j in range(K):
#             s += grid[x+i][y+j]
#     return s

# def solution(grid, K):
#     answer = 0
#     n = len(grid)
    
#     A = 0
#     B = 0
#     for i in range(n-K+1):
#         for j in range(n-K+1):
#             A = calc(grid, i, j, K)
#             idxStore = []
#             for x in range(-K+1,K):
#                 for y in range(-K+1,K):
#                     idxStore.append([i+x, j+y])
#             for p in range(n-K+1):
#                 for q in range(n-K+1):
#                     if [p, q] not in idxStore:
#                         B = calc(grid, p, q, K)
#                         answer = max(answer, A+B)

#     return answer

# 카카오커머스 3번

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

# 백 엔드 1번

# def solution(lottos, win_nums):
    
#     count = 0

#     for temp in lottos:
#         if temp in win_nums:
#             count += 1

#     # if count + lottos.count(0) <= 1:
#     #     best = 6
#     # else:
#     #     best = 7 - (count + lottos.count(0))

#     best = 7 - (count + lottos.count(0)) if count + lottos.count(0) > 1 else 6
    
#     # if count <= 1:
#     #     worst = 6
#     # else:
#     #     worst = 7 - count

#     worst = 7 - count if count > 1 else 6

#     return [best, worst]

# 백 엔드 2번

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

# 백 엔드 3번

def solution(enroll, referral, seller, amount):
    
    money_dict = dict()
    
    for name in enroll:
        money_dict[name] = 0
    
    for who, count in zip(seller, amount):
        cost = count * 100
        name = who
        while name != "-":
            money_dict[name] += round(cost * 0.9)
            cost = round(cost * 0.1)
            name = referral[enroll.index(name)]
        
    return list(money_dict.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], 
["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))

# 백 엔드 4번

# select id, 뭐시기, host_id from places where host_id in (select host_id from places group by host_id having count(*) >= 2) order by id;