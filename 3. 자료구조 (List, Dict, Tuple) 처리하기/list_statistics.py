while True:
    # 사용자에게 숫자 입력을 요청합니다.
    input_str = input("5개의 숫자를 공백으로 구분하여 입력하세요 (예: 10 20 30 40 50): ")

    # 입력받은 문자열을 공백 기준으로 나누어 리스트로 만듭니다.
    str_numbers = input_str.split()

    # 입력된 숫자의 개수가 5개가 아니면 오류 메시지를 출력하고 다시 시작합니다.
    if len(str_numbers) != 5:
        print("\n⚠️ 오류: 반드시 5개의 숫자를 입력해야 합니다.\n")
        continue

    try:
        # 문자열 리스트를 숫자(float) 리스트로 변환합니다.
        # float을 사용하면 10.5와 같은 소수도 처리할 수 있습니다.
        numbers = [float(n) for n in str_numbers]

        # 합계 계산: 내장 함수 sum() 사용
        total = sum(numbers)

        # 평균 계산: 합계 / 개수
        average = total / len(numbers)

        # 결과 출력
        print(f"\n입력된 리스트: {numbers}")
        print(f"합계: {total}")
        print(f"평균: {average}")

    except ValueError:
        # 숫자로 변환할 수 없는 값이 포함된 경우 오류 메시지를 출력합니다.
        print("\n⚠️ 오류: 숫자로만 입력해주세요.\n")
        continue

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30) # 다음 실행 전 구분을 위한 라인