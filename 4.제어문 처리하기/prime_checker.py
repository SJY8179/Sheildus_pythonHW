import math

def is_prime(number):
    """숫자가 소수인지 판별하는 함수"""
    # 1 이하의 숫자는 소수가 아닙니다.
    if number < 2:
        return False
    
    # 2부터 해당 숫자의 제곱근까지만 확인하면 됩니다.
    # int(math.sqrt(number)) + 1
    for i in range(2, int(math.sqrt(number)) + 1):
        # 나누어 떨어지는 수가 있으면 소수가 아닙니다.
        if number % i == 0:
            return False
            
    # 위의 반복문에서 나누어 떨어지는 수가 없으면 소수입니다.
    return True

# --- 메인 프로그램 루프 ---
while True:
    try:
        num_input = int(input("소수인지 판별할 숫자를 입력하세요: "))
        
        # is_prime 함수를 호출하여 결과를 확인합니다.
        if is_prime(num_input):
            print(f" {num_input}은(는) 소수입니다.")
        else:
            print(f" {num_input}은(는) 소수가 아닙니다.")

    except ValueError:
        print(" 정수만 입력해주세요.\n")
        continue

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 판별하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)