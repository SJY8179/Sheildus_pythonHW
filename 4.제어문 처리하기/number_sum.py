# 전체 프로그램을 반복하기 위한 외부 루프
while True:
    # 계산을 시작할 때마다 합계와 입력 리스트를 초기화합니다.
    total = 0
    numbers_entered = []
    
    print("--- 0 입력 시까지 숫자 더하기 ---")
    
    # 숫자 입력을 받기 위한 내부 루프
    while True:
        try:
            num = float(input("더할 숫자를 입력하세요 (0 입력 시 종료): "))
            
            # 0이 입력되면 내부 루프를 종료합니다.
            if num == 0:
                break
            
            # 입력된 숫자를 합계에 더하고 리스트에 추가합니다.
            total += num
            numbers_entered.append(num)
            
        except ValueError:
            print(" 숫자로만 입력해주세요.")

    # --- 최종 계산 결과 출력 ---
    print("\n--- 🧾 계산 결과 ---")
    if not numbers_entered:
        print("입력된 숫자가 없습니다.")
    else:
        print(f"입력된 숫자들: {numbers_entered}")
        print(f"총 합계: {total}")
        
    # 사용자에게 새로운 계산을 시작할지 묻습니다.
    if input("\n새로운 계산을 시작하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("="*30)