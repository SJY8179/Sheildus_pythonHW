while True:
    # 사용자로부터 공백으로 구분된 숫자들을 입력받습니다.
    input_str = input("숫자들을 공백으로 구분하여 입력하세요: ")
    if not input_str:
        print(" 숫자를 입력해주세요.\n")
        continue

    try:
        # 입력받은 문자열을 숫자(float) 리스트로 변환합니다.
        numbers = [float(n) for n in input_str.split()]
    except ValueError:
        print(" 숫자로만 입력해주세요.\n")
        continue

    print(f"\n입력된 리스트: {numbers}\n")

    # --- 1. filter()로 짝수만 걸러내기 ---
    print("## filter(): 짝수만 걸러내기")
    even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
    print(f"  결과: {even_numbers}")

    print("-" * 40)

    # --- 2. map()으로 모든 숫자 제곱하기 ---
    print("## map(): 모든 숫자를 제곱하기")
    squared_numbers = list(map(lambda n: n**2, numbers))
    print(f"  결과: {squared_numbers}")
    
    print("-" * 40)

    # --- 3. filter와 map 함께 사용하기 ---
    print("## filter와 map 함께 사용: 짝수만 제곱하기")
    squared_even_numbers = list(map(lambda n: n**2, filter(lambda n: n % 2 == 0, numbers)))
    print(f" 결과: {squared_even_numbers}")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)