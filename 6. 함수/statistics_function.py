import math

def calculate_stats(num_list):
    """
    숫자 리스트를 받아 평균, 최댓값, 최솟값, 표준편차를 
    딕셔너리로 반환합니다.
    """
    # 리스트가 비어있으면 계산이 불가능하므로 None을 반환합니다.
    if not num_list:
        return None
    
    n = len(num_list)
    
    # 평균, 최댓값, 최솟값 계산
    mean = sum(num_list) / n
    max_val = max(num_list)
    min_val = min(num_list)
    
    # 표준편차 계산
    # 1. 각 숫자와 평균의 차이를 제곱하여 모두 더합니다 (분산).
    variance = sum((x - mean) ** 2 for x in num_list) / n
    # 2. 분산에 제곱근을 씌웁니다.
    std_dev = math.sqrt(variance)
    
    # 결과를 딕셔너리로 묶어 반환합니다.
    return {
        'mean': mean,
        'max': max_val,
        'min': min_val,
        'std_dev': std_dev
    }

# --- 메인 프로그램 루프 ---
while True:
    input_str = input("통계를 계산할 숫자들을 공백으로 구분하여 입력하세요: ")
    if not input_str:
        print(" 숫자를 입력해주세요.\n")
        continue
        
    try:
        numbers = [float(n) for n in input_str.split()]
    except ValueError:
        print(" 숫자로만 입력해주세요.\n")
        continue
    
    # 함수를 호출하여 통계 정보를 받습니다.
    stats = calculate_stats(numbers)
    
    # --- 결과 출력 ---
    if stats:
        print("\n---  통계 정보 ---")
        print(f"입력된 리스트: {numbers}")
        # 소수점 둘째 자리까지 반올림하여 표시합니다.
        print(f"평균: {stats['mean']:.2f}")
        print(f"최댓값: {stats['max']}")
        print(f"최솟값: {stats['min']}")
        print(f"표준편차: {stats['std_dev']:.2f}")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 계산하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)