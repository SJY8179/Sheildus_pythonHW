import math

# --- 함수 정의 (모듈의 역할) ---

def circle_area(radius):
    """원의 넓이를 계산합니다."""
    return math.pi * (radius ** 2)

def rectangle_area(width, height):
    """직사각형의 넓이를 계산합니다."""
    return width * height

def factorial(n):
    """팩토리얼을 계산합니다."""
    if n < 0:
        return "오류: 음수 입력"
    return math.factorial(n)

def gcd(a, b):
    """두 수의 최대공약수를 계산합니다."""
    return math.gcd(a, b)


# --- 메인 프로그램 실행 부분 ---
# 이 파이썬 파일이 직접 실행되었을 때만 아래 코드가 실행됩니다.
if __name__ == "__main__":
    
    while True:
        print("\n---  원하시는 계산을 선택하세요 ---")
        print("1. 원의 넓이")
        print("2. 직사각형 넓이")
        print("3. 팩토리얼 (n!)")
        print("4. 최대공약수 (GCD)")
        print("5. 종료")
        
        choice = input("선택 (1-5): ")

        try:
            if choice == '1':
                r = float(input("반지름을 입력하세요: "))
                print(f"  결과: 원의 넓이는 {circle_area(r):.2f} 입니다.")
            
            elif choice == '2':
                w = float(input("가로 길이를 입력하세요: "))
                h = float(input("세로 길이를 입력하세요: "))
                print(f"  결과: 직사각형의 넓이는 {rectangle_area(w, h)} 입니다.")

            elif choice == '3':
                n = int(input("팩토리얼을 계산할 정수를 입력하세요: "))
                print(f"  결과: {n}! = {factorial(n)} 입니다.")

            elif choice == '4':
                a = int(input("첫 번째 정수를 입력하세요: "))
                b = int(input("두 번째 정수를 입력하세요: "))
                print(f"  결과: {a}와(과) {b}의 최대공약수는 {gcd(a, b)} 입니다.")

            elif choice == '5':
                print("프로그램을 종료합니다.")
                break
            
            else:
                print(" 1~5 사이의 숫자를 입력해주세요.")

        except ValueError:
            print(" 잘못된 값을 입력했습니다. 다시 시도해주세요.")
        
        print("-" * 30)