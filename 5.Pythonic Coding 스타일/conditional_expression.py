while True:
    try:
        age = int(input("나이를 입력하세요: "))
    except ValueError:
        print("⚠️ 숫자로만 입력해주세요.\n")
        continue

    # --- 1. 일반적인 if-else 문 ---
    if age >= 19:
        status_a = "성인"
    else:
        status_a = "미성년자"
    print(f"일반 if-else 결과: 당신은 {status_a}입니다.")


    # --- 2. 조건부 표현식 (삼항 연산자) ---
    status_b = "성인" if age >= 19 else "미성년자"
    print(f"조건부 표현식 결과: 당신은 {status_b}입니다.")


    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 판별하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)