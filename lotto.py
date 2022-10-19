# 응용문제 7 -로또 맞춰보기 예제
# 1. 6개의 숫자 입력받기

# 6개의 숫자를 담을 list 생성

import email
from genericpath import samefile
from operator import is_
from re import M
from random import randint, random, sample


my_lotto_numbers = list()

# 6번 숫자를 입력 : for

for i in range(6):
    # 정수 입력 => 조건에 맞는 숫자가 입력될때 까지 반복
    # 몇번 입력해야 OK인지 알수 없다 => while True : 사용

    while True:
        input_num = int(input(f'{i+1}번째 로또 번호 입력 : '))

        # 받아낸 input_number가 제대로 되었다면? 무한반복 종료 => 다음 숫자 받으러.
        
        # 반복종료 조건 1. 1~45 이내?
        # 1 <= 입력값 and 입력값 <= 45
        is_range_ok = (1<= input_num) and (input_num <= 45)

        # 무한반복 종료 조건 2. 이미 등록한 번호가 아니어야 함.
        # 중복인가? 내 로또 번호에 이미, 입력값이 들어있는가?
        # input_num이 my_lott_num 안에 포함되어있는가?
        is_duplicated = input_num in my_lotto_numbers

        if is_range_ok and (not is_duplicated): 
            # 검사 통과시 무한반복 종료
            # 입력값을, 내 로또 번호로 등록 => 중복검사에도 활용 가능
            my_lotto_numbers.append( input_num )
            break
        elif is_duplicated:
            # 중복검사에서 탈락됨
            print('이미 등록된 숫자 입니다.')
        else :
            # 범위 검사 탈락시 안내문구
            print('1~45의 값만 입력 가능합니다.')
            # 다시 입력 시킨다 => 무한반복 유지 => break X

# 입력한 숫자 목록 확인
print(f'내 숫자 목록 : {my_lotto_numbers}')

# 숫자 목록을 작은 수 ~ 큰 수로 정렬. (sort)

# bubble sort 구현해보기

# 2개씩 짝지어 비교 => 순서가 잘못됬으면 서로 위치 변경 => 통째로 6번 반복

# 총 6개의 숫자를 모두 뽑아서 확인
for idx, val in enumerate(my_lotto_numbers):
    
    # 2개씩 뽑아서 비교
    for j in range(5):
        # 5회반복시 : 0,1번 비교> 1,2번 비교... 4,5번 비교에서 마무리

        # 순서가 잘못되었나? 앞의 숫자가 더 큰가?
        if my_lotto_numbers[j] > my_lotto_numbers[j+1] :
            # 두 자료의 위치를 변경
            # 두 변수의 위치 바꿔주기

            backup = my_lotto_numbers[j]
            my_lotto_numbers[j] = my_lotto_numbers[j+1]
            my_lotto_numbers[j+1] = backup
# 정렬 되었는지?

print(my_lotto_numbers)            

# CPU가 숫자 6개 당첨 작업
# 1~45의 범위 + 중복 X.

# 파이썬의 sample 기능 활용 random 추출 / 6개 중복 X
win_number_list = sample (range(1, 46), 6)


print(f'당첨 번호 : {win_number_list}')

# 당첨 번호도 순서대로 정리 - 파이썬 제공 기능 활용

win_number_list.sort()

# 당첨번호 6개 생성 이후, 보너스번호 하나 추가 생성
# 기존 당첨번호와 중복되면 안됨.

while True : 
    # 1~45의 랜덤을 쉽게 뽑는 방법?
    rand_num = randint(1, 45)

    is_already_num = rand_num in win_number_list

    if not is_already_num :
        # 보너스번호로 등록
        # 무한반복 종료
        bonus_num = rand_num
        break


# 임시 처리 : 당첨번호 / 보너스번호를 고정해둬야 테스트 하기 편하다.

# win_number_list = [10,15,20,25,30,35]
# bonus_num = 40

print(win_number_list)

print(bonus_num)
# 내 번호 목록 / 당첨 번호 목록 중 같은 갯수?

correct_count = 0

# 내 번호를 하나씩 꺼내서(반복) => 당첨번호 안에 있는가? 질문
# my_number_list => list로 되어있다.

for my_num in my_lotto_numbers:
    # 하나씩 꺼내는 my_num이 당첨번호에 포함되어있나?
    if my_num in win_number_list:
        correct_count += 1 # 맞춘 숫자 하나 더 발견!

# 갯수에 따른 등수 판정

if correct_count == 6:
    print('1등')
elif correct_count == 5:
    # 보너스 번호 추가 검사 필요

    # 보너스번호를 맞췄다면 2등
    # 아니면 3등 처리
    if bonus_num in my_lotto_numbers :
        print('2등')
    else :
        print('3등')
elif correct_count == 4:
    print('4등')
elif correct_count == 3:
    print('5등')
else : 
    print('낙첨')