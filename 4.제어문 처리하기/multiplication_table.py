while True:
    try:
        # 사용자로부터 단수를 입력받아 정수(int)로 변환합니다.
        dan = int(input("출력할 단수를 입력하세요: "))
        
        print(f"\n--- {dan}단 ---")
        # for 반복문으로 1부터 9까지의 곱을 계산하고 출력합니다.
        for i in range(1, 10):
            print(f"{dan} x {i} = {dan * i}")

    except ValueError:
        print(" 숫자로만 입력해주세요.\n")
        continue

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다른 단도 출력하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 20)