import csv

def write_scores_to_csv(filename, header, data):
    """학생 성적 데이터를 CSV 파일에 저장합니다."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)
        print(f"\n '{filename}' 파일에 데이터를 성공적으로 저장했습니다.")
    except IOError as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")

def read_and_calculate_average(filename):
    """CSV 파일을 읽어 점수 평균을 계산합니다."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            scores = [int(row[2]) for row in reader]
            
            if scores:
                return sum(scores) / len(scores)
            return None
    except (IOError, FileNotFoundError, ValueError, IndexError):
        return None

# --- 메인 프로그램 루프 ---
while True:
    # --- 1. 사용자로부터 데이터 입력받기 ---
    student_data = []
    print("---  학생 성적 입력 ---")
    print("학생 이름에 '완료'를 입력하면 입력을 종료하고 파일을 생성합니다.")
    
    while True:
        name = input("학생 이름을 입력하세요: ")
        if name.lower() == '완료':
            break
        
        subject = input(f"'{name}' 학생의 과목을 입력하세요: ")
        
        while True:
            try:
                score = int(input(f"'{name}' 학생의 '{subject}' 점수를 입력하세요: "))
                break
            except ValueError:
                print(" 점수는 숫자로만 입력해주세요.")
        
        student_data.append([name, subject, score])
        print(f" '{name}' 학생의 정보가 추가되었습니다.\n")

    # --- 2. 입력된 데이터로 파일 쓰고 평균 계산하기 ---
    if not student_data:
        print("\n입력된 데이터가 없습니다.")
    else:
        file_to_save = 'student_grades_input.csv'
        csv_header = ['name', 'subject', 'score']
        
        write_scores_to_csv(file_to_save, csv_header, student_data)
        
        print("\n--- 평균 점수 계산 ---")
        average_score = read_and_calculate_average(file_to_save)
        
        if average_score is not None:
            print(f"📈 전체 학생의 평균 점수는 {average_score:.2f}점 입니다.")
        else:
            print("평균을 계산할 수 없습니다.")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n새로운 데이터로 다시 시작하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)