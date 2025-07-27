while True:
    # 사용자로부터 공백으로 구분된 숫자들을 입력받습니다.
    input_str = input("숫자들을 공백으로 구분하여 입력하세요 (예: 10 4 8 2 9): ")
    
    try:
        # 입력받은 문자열을 숫자(float) 리스트로 변환합니다.
        numbers = [float(n) for n in input_str.split()]
        
        # 고유한 숫자가 2개 이상 있는지 확인합니다.
        unique_numbers = list(set(numbers))
        if len(unique_numbers) < 2:
            print("\n오류: 두 번째로 큰 값을 찾으려면 고유한 숫자가 2개 이상 필요합니다.\n")
            continue

        # 1. 최댓값 찾기
        max_val = max(numbers)
        
        # 2. 최솟값 찾기
        min_val = min(numbers)
        
        # 3. 두 번째로 큰 값 찾기
        #    - set()으로 중복을 제거하고 list()로 다시 변환합니다.
        #    - reverse=True로 내림차순 정렬을 합니다. (예: [10, 9, 8, 4, 2])
        #    - 정렬된 리스트의 두 번째 값(인덱스 1)을 가져옵니다.
        sorted_unique_numbers = sorted(unique_numbers, reverse=True)
        second_largest_val = sorted_unique_numbers[1]
        
        # --- 결과 출력 ---
        print(f"\n입력된 리스트: {numbers}")
        print("-" * 25)
        print(f" 최댓값: {max_val}")
        print(f" 최솟값: {min_val}")
        print(f" 두 번째로 큰 값: {second_largest_val}")
        
    except ValueError:
        print("\n오류: 숫자로만 입력해주세요.\n")
        continue

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)