while True:
    # 매번 새로운 실행을 위해 빈 리스트로 시작합니다.
    students = []

    print("--- 📖 학생 정보 입력 시작 ---")
    print("학생 이름에 '완료'를 입력하면 입력을 종료하고 정렬을 시작합니다.")

    # 학생 정보 입력을 위한 내부 반복문
    while True:
        # 학생 이름 입력받기
        name = input("학생 이름을 입력하세요: ")

        # '완료'를 입력하면 학생 정보 입력을 중단합니다.
        if name == '완료':
            break

        # 학생 나이 입력받기 (숫자가 아니면 다시 입력)
        while True:
            try:
                age = int(input(f"'{name}' 학생의 나이를 입력하세요: "))
                break  # 올바른 나이가 입력되면 나이 입력 반복문 탈출
            except ValueError:
                print(" 나이는 숫자로만 입력해주세요.")
        
        # 입력받은 정보로 딕셔너리를 만들어 students 리스트에 추가합니다.
        students.append({'name': name, 'age': age})
        print(f" '{name}' 학생 정보가 추가되었습니다.\n")

    # 입력된 학생이 있는지 확인 후 정렬 및 출력
    if students:
        print("\n---  정렬 전 ---")
        for student in students:
            print(f"이름: {student['name']}, 나이: {student['age']}")

        # lambda 함수를 key로 사용하여 나이('age') 순으로 리스트를 정렬합니다.
        sorted_students = sorted(students, key=lambda item: item['age'])

        print("\n---  나이 순 오름차순 정렬 후 ---")
        for student in sorted_students:
            print(f"이름: {student['name']}, 나이: {student['age']}")
    else:
        print("\n입력된 학생 정보가 없습니다.")

    # 전체 프로그램을 다시 실행할지 묻습니다.
    if input("\n새로운 정보로 다시 시작하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)