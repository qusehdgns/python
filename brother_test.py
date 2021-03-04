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

import sys
num = int(sys.stdin.readline().rstrip())
count = 0
calc = num

while True:
    count += 1
    temp = (calc//10) + (calc%10)
    calc = (calc%10) + (temp%10)
    print(calc)
    if num == calc:
        break
        
print(count)