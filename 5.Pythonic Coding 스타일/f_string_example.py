while True:
    # --- 사용자로부터 정보 입력받기 ---
    name = input("이름을 입력하세요: ")
    
    while True:
        try:
            age = int(input("나이를 입력하세요: "))
            break
        except ValueError:
            print(" 나이는 숫자로만 입력해주세요.")
            
    while True:
        try:
            money = int(input("월급을 입력하세요 (예: 3500000): "))
            break
        except ValueError:
            print(" 월급은 숫자로만 입력해주세요.")

    # --- f-string을 사용한 다양한 포매팅 결과 ---
    print("\n" + "="*30)
    print("      f-string 포매팅 결과")
    print("="*30)

    # 1. 기본 변수 사용
    print(f"1. 기본 출력: 안녕하세요, {name}님! {age}살이시군요.")

    # 2. 표현식 사용 (f-string 안에서 간단한 계산 가능)
    print(f"2. 표현식 사용: {name}님의 10년 후 나이는 {age + 10}살입니다.")

    # 3. 함수 호출 (f-string 안에서 함수 사용 가능)
    print(f"3. 함수 호출: 이름(영문 대문자): {name.upper()}")

    # 4. 숫자 서식 지정
    #    - `{변수:,}`: 천 단위 쉼표
    #    - `{변수:0_d}`: _자리 수 확보, 빈자리는 0으로 채움
    print(f"4. 숫자 서식: {name}님의 월급은 {money:,}원입니다.")
    print(f"   - 나이를 5자리로 표현하면? -> {age:05d}")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)