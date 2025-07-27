while True:
    # 사용자로부터 공백으로 구분된 요소들을 입력받습니다.
    input_str = input("리스트 요소들을 공백으로 구분하여 입력하세요 (예: 8 a 2 8 c a): ")
    
    # 입력받은 문자열을 공백 기준으로 나누어 리스트로 만듭니다.
    original_list = input_str.split()
    
    # 입력된 요소가 있는지 확인합니다.
    if not original_list:
        print("\n 하나 이상의 요소를 입력해주세요.\n")
        continue

    # 1. set()으로 변환하여 중복을 제거합니다.
    # 2. sorted() 함수로 그 결과를 바로 정렬합니다.
    unique_sorted_list = sorted(set(original_list))
    
    # --- 결과 출력 ---
    print(f"\n원본 리스트: {original_list}")
    print(f" 중복 제거 및 정렬 후: {unique_sorted_list}")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)