while True:
    # 첫 번째 리스트를 입력받습니다.
    input_str1 = input("첫 번째 리스트의 요소들을 공백으로 구분하여 입력하세요: ")
    list1 = input_str1.split()

    # 두 번째 리스트를 입력받습니다.
    input_str2 = input("두 번째 리스트의 요소들을 공백으로 구분하여 입력하세요: ")
    list2 = input_str2.split()
    
    # 두 리스트 중 하나라도 비어있으면 다시 시작합니다.
    if not list1 or not list2:
        print("\n 두 리스트 모두 하나 이상의 요소를 입력해야 합니다.\n")
        continue

    # 1. 리스트 병합
    # '+' 연산자를 사용하여 두 리스트를 합칩니다.
    merged_list = list1 + list2
    
    # 2. 공통 요소 찾기
    # set으로 변환 후 '&' 연산자(교집합)를 사용하면 매우 효율적입니다.
    # 최종적으로 list()를 이용해 다시 리스트로 만듭니다.
    common_elements = list(set(list1) & set(list2))
    
    # --- 결과 출력 ---
    print("\n" + "="*30)
    print("결과")
    print("="*30)
    print(f"리스트 1: {list1}")
    print(f"리스트 2: {list2}")
    print("-" * 30)
    print(f" 병합된 리스트: {merged_list}")
    
    if common_elements:
        print(f" 공통 요소: {common_elements}")
    else:
        print(" 공통 요소: 없음")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("\n")