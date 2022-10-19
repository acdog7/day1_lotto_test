# 응용문제 7 -로또 맞춰보기 예제
# 1. 6개의 숫자 입력받기

# 6개의 숫자를 담을 list 생성

my_lotto_numbers = list()

# 6번 숫자를 입력 : for

for i in range(6):
    # 정수 입력
    input_num = int(input(f'{i+1}번째 로또 번호 입력 : '))