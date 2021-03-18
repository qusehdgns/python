# # 숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# # 문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print('ㅋ'*10)

# # boolean 자료형
# # 참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# # 변수
# # 애완동물을 소개해주세요~
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# hobby = "공놀이"
# # print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# # , 사용시 빈칸 한개씩 포함
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# 주석
''' 여러 문장 주석 처리
하는 방법 입니다 '''

'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명 : station

변수값 : "사당", "신도림", "인천공항" 순서대로 입력

출력 문장 : XX 행 열차가 들어오고 있습니다.
'''

# station = "사당"

# print(station + "행 열차가 들어오고 있습니다.")

# # 연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 몫 구하기 1
# print(10//3) # 3

# print(10 > 3) # True
# print(4 >= 7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print(3 == 3) # True
# print(4 == 2) # False
# print(3 + 4 == 7) # True

# print(1 != 3) # True
# print(not(1 != 3)) # False

# print((3 > 0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True

# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False

# # 간단한 수식
# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 14
# number = 2 + 3 * 4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18
# print(number)
# number -= 2 # 16
# print(number)

# number %= 5 # 0
# print(number)

# # 숫자 처리 함수
# print(abs(-5)) # 절대값 5
# print(pow(4, 2)) # 제곱 4^2 = 4 * 4 = 16
# print(max(5, 12)) # 최댓값 12
# print(min(5, 12)) # 최솟값 5
# print(round(3.14)) # 반올림 3
# print(round(4.99)) # 반올림 5

# from math import *
# print(floor(4.99)) # 내림 4
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) # 제곱근 4

# # 랜덤 함수
# from random import *
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라은으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.
'''
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

# # 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# # 슬라이싱
# jumin = "970422-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지

# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper()) # 대문자 확인
# print(len(python)) # 길이 반환
# print(python.replace("Python", "Java")) # 문자열 변환

# index = python.index("n") # 특정 문자열 인덱스
# print(index)
# index = python.index("n", index + 1) # 두번째 n 탐색
# print(index)

# print(python.find("Java")) # 문자열 없을 시 -1 반환
# # print(python.index("Java")) # 문자열 없을 시 에러 발생

# print(python.count("n")) # 특정 문자열 몇 개 인지 카운트

# # 문자열 포맷
# # print("a" + "b")
# # print("a", "b")

# # 방법 1
# print("나는 %d살입니다." % 20) # 정수
# print("나는 %s을 좋아해요" % "파이썬") # 문자열
# print("Apple은 %c로 시작해요." % "A") # 문자

# print("나는 %s살입니다." % 20) # 정수형 문자열로도 가능
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 2개 동시

# # 방법 2
# print("나는 {}살입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 순서를 지정 출력
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간")) # format 내부 변수를 선언하여 사용 가능
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") # 실제 변수로 사용 가능

# # 탈출 문자
# print("백문이 불여일견\n백견이 불여일타") # 줄바꿈

# print("저는 \"변동훈\"입니다.") # 따옴표
# print('저는 "변동훈"입니다.')
# print("저는 \'변동훈\'입니다.")

# print("C:\\Users\\qusehdgns\\Desktop>") # 역슬래쉬

# print("Red Apple\rPind") # 커서 맨앞으로 이동

# print("Redd\bApple") # 한글자 앞으로 이동

# print("Red\tApple") # 탭

'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                    (nav)               (5)         (1)                 (!)
예) 생성된 비밀번호 : nav51!
'''
# # url = "http://naver.com"
# url = "http://youtube.com"
# my_str = url.replace("http://", "") # 규칙1
# my_str = my_str[:my_str.index(".")] # 규칙2

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다".format(url, password))

# # 리스트 []

# # 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# # print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 딕셔너리

# cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(100))

# print(cabinet[5]) # 값 없을 시 에러 발생 후 종료
# print(cabinet.get(5, "사용 가능")) # 값 없을 시 None 출력 및 default 값 설정
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

# 튜플 - 리스트와 유사하지만 변경할 수 없고 빠름

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# 추가 불가
# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 집합(set)
# 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "조세호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 출력
# print(java & python)
# print(java.intersection(python))

# # 합집합 출력
# print(java | python)
# print(java.union(python))

# # 차집합 출력
# print(java - python)
# print(java.difference(python))

# # 추가
# python.add("김태호")
# print(python)

# # 삭제
# java.remove("김태호")
# print(java)

# def test(*a, b = 3):
#     for temp in a:
#         print(f"a:{temp}", end=" ")
#     else:
#         print()
#     print(f"b:{temp}")

# test(*a=1,*a=2,*a=3,*a=4,*a=5,b=5)
# test(1)

# def test(*a):
#     return type(a)

# print(test(1,2,3,4))

# a = 10

# for _ in range(1):
#     a = 8

# print(a)

# a = { 1, 2, 3}

# print(type(a))

