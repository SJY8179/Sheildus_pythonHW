while True:
    # 매번 새로운 계산을 위해 빈 딕셔너리로 시작합니다.
    student_scores = {}

    print("--- 학생 성적 입력 시작 ---")
    print("학생 이름에 '끝'을 입력하면 입력을 종료하고 계산을 시작합니다.")

    # 학생 정보 입력을 위한 내부 반복문
    while True:
        # 학생 이름 입력받기
        name = input("학생 이름을 입력하세요: ")

        # '끝'을 입력하면 학생 정보 입력을 중단합니다.
        if name == '끝':
            break

        # 학생 점수 입력받기 (숫자가 아니면 다시 입력)
        while True:
            try:
                score = int(input(f"'{name}' 학생의 점수를 입력하세요: "))
                student_scores[name] = score
                break  # 올바른 점수가 입력되면 점수 입력 반복문 탈출
            except ValueError:
                print("⚠️ 점수는 숫자로만 입력해주세요.")
    
    # 입력된 학생 정보(딕셔너리)를 기반으로 계산 시작
    print("\n--- 계산 결과 ---")
    if student_scores:
        # 입력된 학생 정보 출력
        print("입력된 성적 정보:")
        for name, score in student_scores.items():
            print(f"  {name}: {score}점")

        scores = student_scores.values()
        total_score = sum(scores)
        average_score = total_score / len(scores)

        print(f"\n총 학생 수: {len(scores)}명")
        print(f"성적 총합: {total_score}점")
        print(f"성적 평균: {average_score:.2f}점")
    else:
        print("입력된 성적 데이터가 없습니다.")

    # 전체 프로그램을 다시 실행할지 묻습니다.
    if input("\n새로운 정보로 다시 계산하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)