# 'message' 매개변수에 "안녕하세요"라는 기본값을 설정합니다.
def generate_greeting(name, message="안녕하세요"):
    """
    인사말을 생성합니다. 
    message가 제공되지 않으면 기본값을 사용합니다.
    """
    return f"{message}, {name}님!"

# --- 메인 프로그램 루프 ---
while True:
    user_name = input("이름을 입력하세요: ")
    custom_message = input("특별한 인사말을 입력하세요 (없으면 Enter 키 입력): ")

    # --- 함수 호출 ---
    if custom_message:
        # 특별한 인사말이 있으면 기본값을 무시하고 입력된 값을 사용합니다.
        greeting = generate_greeting(user_name, custom_message)
    else:
        # 특별한 인사말이 없으면 'message'의 기본값이 사용됩니다.
        greeting = generate_greeting(user_name)
        
    print(f"\n결과: {greeting}")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)