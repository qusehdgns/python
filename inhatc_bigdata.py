# 1 번 문제
print("1번 문제")
while True:
    # 한줄에 2수 띄어쓰기 입력
    no1, no2 = map(int, input().split())

    if no1 == 0 and no2 == 0:
        break

    print(f'{no1} + {no2} = {no1 + no2}')
    print(f'{no1} - {no2} = {no1 - no2}')
    print(f'{no1} * {no2} = {no1 * no2}')

    if no2 != 0:
        print(f'{no1} / {no2} = {no1 // no2}')
        print(f'{no1} % {no2} = {no1 % no2}')


# 2번 문제
print("2번 문제")
while True:
    # 한줄에 2수 띄어쓰기 입력
    no = list(map(int, input().split()))

    if no[0] == 0 and no[1] == 0:
        break
    
    print(f'{no[0]} + {no[1]} = {no[0] + no[1]}')
    print(f'{no[0]} - {no[1]} = {no[0] - no[1]}')
    print(f'{no[0]} * {no[1]} = {no[0] * no[1]}')

    if no[1] != 0:
        print(f'{no[0]} / {no[1]} = {no[0] // no[1]}')
        print(f'{no[0]} % {no[1]} = {no[0] % no[1]}')