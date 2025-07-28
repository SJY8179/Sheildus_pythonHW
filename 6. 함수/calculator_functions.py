# 덧셈 함수
def add(a, b):
    return a + b

# 뺄셈 함수
def subtract(a, b):
    return a - b

# 곱셈 함수
def multiply(a, b):
    return a * b

# 나눗셈 함수
def divide(a, b):
    # 0으로 나누는 것을 방지
    if b == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return a / b

# --- 메인 프로그램 루프 ---
while True:
    try:
        # 사용자로부터 두 개의 숫자를 입력받아 실수(float)로 변환합니다.
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
    except ValueError:
        print(" 숫자로만 입력해주세요.\n")
        continue

    # --- 함수 호출 및 결과 출력 ---
    print("\n---  사칙연산 결과 ---")
    print(f"덧셈 ({num1} + {num2}) = {add(num1, num2)}")
    print(f"뺄셈 ({num1} - {num2}) = {subtract(num1, num2)}")
    print(f"곱셈 ({num1} * {num2}) = {multiply(num1, num2)}")
    print(f"나눗셈 ({num1} / {num2}) = {divide(num1, num2)}")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 계산하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)