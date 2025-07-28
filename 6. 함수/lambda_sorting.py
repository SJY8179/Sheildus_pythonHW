while True:
    # 새로운 실행을 위해 빈 리스트로 시작합니다.
    students = []

    print("--- 📖 학생 정보 입력 시작 ---")
    print("학생 이름에 '완료'를 입력하면 입력을 종료하고 정렬을 시작합니다.")

    # 학생 정보 입력을 위한 내부 반복문
    while True:
        name = input("학생 이름을 입력하세요: ")
        if name == '완료':
            break

        while True:
            try:
                age = int(input(f"'{name}' 학생의 나이를 입력하세요: "))
                break
            except ValueError:
                print(" 나이는 숫자로만 입력해주세요.")
        
        while True:
            try:
                score = int(input(f"'{name}' 학생의 점수를 입력하세요: "))
                break
            except ValueError:
                print(" 점수는 숫자로만 입력해주세요.")

        # 입력받은 정보를 튜플로 만들어 리스트에 추가합니다.
        students.append((name, age, score))
        print(f" '{name}' 학생 정보가 추가되었습니다.\n")

    # 입력된 학생이 있는지 확인 후 정렬 및 출력
    if students:
        print("\n" + "="*30)
        print("     정렬 결과")
        print("="*30)

        # 1. 이름 오름차순 정렬
        print("\n## 1. 이름 오름차순 정렬")
        sorted_by_name = sorted(students, key=lambda s: s[0])
        for student in sorted_by_name:
            print(student)

        # 2. 나이 오름차순 정렬
        print("\n## 2. 나이 오름차순 정렬")
        sorted_by_age = sorted(students, key=lambda s: s[1])
        for student in sorted_by_age:
            print(student)

        # 3. 점수 내림차순 정렬
        print("\n## 3. 점수 내림차순 정렬")
        sorted_by_score_desc = sorted(students, key=lambda s: s[2], reverse=True)
        for student in sorted_by_score_desc:
            print(student)
    else:
        print("\n입력된 학생 정보가 없습니다.")

    # 전체 프로그램을 다시 실행할지 묻습니다.
    if input("\n새로운 정보로 다시 시작하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("\n")