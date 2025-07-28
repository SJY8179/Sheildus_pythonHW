import random
import datetime

def generate_random_number(min_val, max_val):
    """지정된 범위 내에서 임의의 정수를 생성합니다."""
    return random.randint(min_val, max_val)

def generate_random_date(start_date, end_date):
    """지정된 두 날짜 사이에서 임의의 날짜를 생성합니다."""
    # 두 날짜 사이의 총 일수 계산
    time_delta = end_date - start_date
    total_days = time_delta.days
    
    # 0과 총 일수 사이의 임의의 숫자 선택
    random_days = random.randrange(total_days)
    
    # 시작 날짜에 임의의 일수를 더하여 최종 날짜 생성
    random_date = start_date + datetime.timedelta(days=random_days)
    
    return random_date

# --- 메인 프로그램 실행 ---
if __name__ == "__main__":
    
    # 1. 임의의 숫자 생성
    min_num, max_num = 1, 1000
    random_number = generate_random_number(min_num, max_num)
    
    print("## 1. 임의의 숫자 생성")
    print(f"  범위 ({min_num} ~ {max_num})에서 생성된 숫자: {random_number}")

    print("-" * 40)

    # 2. 임의의 날짜 생성
    start = datetime.date(2024, 1, 1)
    end = datetime.date(2025, 12, 31)
    random_date = generate_random_date(start, end)
    
    print("## 2. 임의의 날짜 생성")
    print(f"  범위 ({start} ~ {end})에서 생성된 날짜: {random_date}")