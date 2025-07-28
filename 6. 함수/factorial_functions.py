# 방법 1: 재귀 함수 사용
def factorial_recursive(n):
    """재귀 호출을 이용해 팩토리얼을 계산합니다."""
    # 0!은 1이고, 재귀를 멈추는 기본 조건(base case)
    if n <= 1:
        return 1
    # n * (n-1)!를 호출하여 결과를 구함
    return n * factorial_recursive(n - 1)

# 방법 2: 반복문 사용
def factorial_iterative(n):
    """for 반복문을 이용해 팩토리얼을 계산합니다."""
    # 곱셈을 위해 결과를 1로 초기화
    result = 1
    # 1부터 n까지의 숫자를 차례로 곱함
    for i in range(1, n + 1):
        result *= i
    return result

# --- 메인 프로그램 루프 ---
while True:
    try:
        num = int(input("팩토리얼을 계산할 양의 정수를 입력하세요: "))
        if num < 0:
            print(" 양의 정수만 입력해주세요.\n")
            continue
    except ValueError:
        print(" 정수만 입력해주세요.\n")
        continue

    # --- 함수 호출 및 결과 출력 ---
    print("\n---  계산 결과 ---")
    print(f"반복문 방식: {factorial_iterative(num)}")
    print(f"재귀 방식:  {factorial_recursive(num)}")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 계산하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)