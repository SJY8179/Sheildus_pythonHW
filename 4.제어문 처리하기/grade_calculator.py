while True:
    try:
        # 사용자로부터 점수를 입력받아 실수(float)로 변환합니다.
        score = float(input("점수를 입력하세요 (0-100): "))

        # 점수가 유효한 범위(0-100)에 있는지 확인합니다.
        if not (0 <= score <= 100):
            print(" 오류: 점수는 0과 100 사이의 숫자여야 합니다.\n")
            continue

        # 학점을 결정할 변수를 초기화합니다.
        grade = ''
        
        # if-elif-else 문으로 점수 구간에 따라 학점을 할당합니다.
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
            
        # 최종 결과를 출력합니다.
        print(f"입력하신 점수 {score}점은 '{grade}' 학점입니다. ✨")

    except ValueError:
        print(" 오류: 숫자로만 입력해주세요.\n")
        continue

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 계산하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)