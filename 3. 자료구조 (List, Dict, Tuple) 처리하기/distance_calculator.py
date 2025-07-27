import math

# 좌표 입력을 처리하는 함수를 만들어 코드를 효율적으로 재사용합니다.
def get_coordinates(prompt):
    """사용자로부터 'x,y' 형식의 좌표를 입력받아 튜플로 반환하는 함수"""
    while True:
        try:
            # 사용자 입력을 콤마(,)를 기준으로 분리합니다.
            input_str = input(prompt)
            parts = input_str.split(',')
            
            # 입력된 값을 실수(float)로 변환합니다.
            x = float(parts[0])
            y = float(parts[1])
            
            # 값이 두 개가 아니면 오류를 발생시킵니다.
            if len(parts) != 2:
                raise IndexError
                
            return (x, y) # (x, y) 튜플을 반환합니다.
        except (ValueError, IndexError):
            print("⚠️ 오류: 'x,y' 형식에 맞춰 숫자를 콤마로 구분해 입력해주세요.\n")

# --- 메인 프로그램 ---
while True:
    # 함수를 호출하여 두 점의 좌표를 입력받습니다.
    point1 = get_coordinates("첫 번째 점의 좌표를 'x,y' 형식으로 입력하세요: ")
    point2 = get_coordinates("두 번째 점의 좌표를 'x,y' 형식으로 입력하세요: ")
    
    # 튜플에서 각 좌표 값을 추출합니다.
    x1, y1 = point1
    x2, y2 = point2
    
    # 거리 공식을 사용하여 거리를 계산합니다.
    # (x2-x1)**2는 (x2-x1)의 제곱을 의미합니다.
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 결과를 출력합니다.
    print(f"\n점 {point1}과(와) 점 {point2} 사이의 거리는 {distance:.2f} 입니다.")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 계산하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)