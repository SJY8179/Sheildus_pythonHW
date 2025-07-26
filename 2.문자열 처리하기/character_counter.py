while True:
    # 사용자로부터 전체 문자열을 입력받습니다.
    main_string = input("문자열을 입력하세요: ")

    # 개수를 셀 특정 문자 또는 문자열을 입력받습니다.
    target_string = input("개수를 셀 문자 또는 문자열을 입력하세요: ")

    # count() 메서드를 사용해 특정 문자열의 개수를 셉니다.
    string_count = main_string.count(target_string)

    # 결과를 출력합니다.
    print(f"\n'{main_string}' 안에는 '{target_string}'이(가) 총 {string_count}번 나타납니다. 🧐")

    # 사용자에게 다시 실행할지 묻습니다.
    # .lower()는 입력값을 소문자로 바꿔 'Y'나 'y' 모두 처리하게 합니다.
    # 'y'가 아니면 break를 통해 while 반복문을 종료합니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break