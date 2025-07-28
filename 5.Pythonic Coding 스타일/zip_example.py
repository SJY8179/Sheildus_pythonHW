while True:
    # 첫 번째 리스트를 사용자로부터 입력받습니다.
    input1 = input("첫 번째 리스트의 요소들을 공백으로 구분하여 입력하세요 (예: 이름1 이름2 이름3): ")
    list1 = input1.split()

    # 두 번째 리스트를 사용자로부터 입력받습니다.
    input2 = input("두 번째 리스트의 요소들을 공백으로 구분하여 입력하세요 (예: 점수1 점수2 점수3): ")
    list2 = input2.split()

    # 두 리스트 중 하나라도 비어있으면 다시 시작합니다.
    if not list1 or not list2:
        print("\n 두 리스트 모두 하나 이상의 요소를 입력해야 합니다.\n")
        continue

    # --- zip()으로 결합하여 출력 ---
    print("\n---  zip 결과 ---")
    print("(두 리스트의 길이가 다를 경우, 더 짧은 쪽에 맞춰집니다.)")
    
    # zip()으로 두 리스트를 짝지어 순회합니다.
    for item1, item2 in zip(list1, list2):
        print(f"{item1} - {item2}")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)