# hour, minute, time = map(int, input().split())
# minute -= (time%60)

# if minute < 0:
#     minute += 60
#     hour -= 1

# hour = (hour - (time//60)) % 24

# print(f"{hour} {minute}")

# n = int(input())
# result = 0

# for i in range(1, n+1):
#     result += i

# print(result)

# n, x = map(int, input().split())
# arr = list(map(int, input().split()))

# result = ""

# for temp in arr[:n]:
#     if temp < x:
#         result += str(temp) + ' '

# print(result)

# num = input()
# count = 0
# calc = num

# if len(num) == 1:
#     num = '0' + num

# while True:
#     count += 1
#     temp = int(calc[0]) + int(calc[1])
#     calc = calc[1] + str(temp)[-1]
#     if num == calc:
#         break
        
# print(count)

# import sys
# num = int(sys.stdin.readline().rstrip())
# count = 0
# calc = num

# while True:
#     count += 1
#     temp = (calc//10) + (calc%10)
#     calc = (calc%10) + (temp%10)
#     print(calc)
#     if num == calc:
#         break
        
# print(count)

# def solution(n):
#     i = 0
#     while 3 ** i <= n:
#         i += 1
        
#     result = []
    
#     tri = [3 ** i for i in range(i)]
    
#     for temp in tri[::-1]:
#         result.append(n // temp)
#         n %= temp
    
#     answer = 0

#     print(tri, result)
    
#     for calc, temp in zip(tri, result):
#         answer += calc * temp
    
#     return answer

# print(solution(45))

# def solution(new_id):
    
#     new_id = new_id.lower()
    
#     result = ''
#     pat = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(10)] + ['-', '_', '.']
    
#     for temp in new_id:
#         if temp in pat:
#             result += temp
            
#     while '..' in result:
#         result = result.replace('..', '.')
    
#     while result[0] == '.' or result[-1] == '.':
#         if result[0] == '.':
#             result = result[1:]
#         elif result[-1] == '.':
#             result = result[:-1]
#         if len(result) == 0:
#             result = 'a'
    
#     return result

# print(solution("=.="))

# def solution(dartResult):

#     calc = []

#     p_pat = ['S', 'D', 'T']
#     c_pat = ['*', '#']

#     temp = ''
#     for i in dartResult:
#         if i in p_pat:
#             if i == 'S':
#                 calc.append(int(temp))
#             elif i == 'D':
#                 calc.append(int(temp) ** 2)
#             else:
#                 calc.append(int(temp) ** 3)
            
#             temp = ''
#         elif i in c_pat:
#             if i == '#':
#                 calc[-1] *= -1
#             else:
#                 if len(calc) >= 2:
#                     calc[-1] *= 2
#                     calc[-2] *= 2
#                 else:
#                     calc[-1] *= 2
#         else:
#             temp += i
    
#     return sum(calc)

# print(solution("1S2D*3T"))

def solution(numbers, hand):
    num_pat = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    
    l_idx = [0, 3]
    r_idx = [2, 3]
    
    result = ''
    
    for num in numbers:
        x, y = 0, 0
        if num in num_pat[0]:
            x = 0
            y = num_pat[0].index(num)
        elif num in num_pat[1]:
            x = 1
            y = num_pat[1].index(num)
        else:
            x = 2
            y = num_pat[2].index(num)
            
        if x == 0:
            result += 'L'
            l_idx = [x, y]
        elif x == 2:
            result += 'R'
            r_idx = [x, y]
        else:
            l_length = abs(x - l_idx[0]) + abs(y - l_idx[1])
            r_length = abs(x - r_idx[0]) + abs(y - r_idx[1])
        
            if l_length < r_length:
                result += 'L'
                l_idx = [x, y]
            elif r_length < l_length:
                result += 'R'
                r_idx = [x, y]
            else:
                if hand == 'right':
                    result += 'R'
                    r_idx = [x, y]
                else:
                    result += 'L'
                    l_idx = [x, y]
        
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))