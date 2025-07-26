# 사용자로부터 이메일 주소를 입력받습니다.
email_address = input("이메일 주소를 입력하세요: ")

# '@' 문자가 포함되어 있는지 확인하여 유효성을 검사합니다.
if '@' in email_address:
    # .split('@', 1)은 '@'를 기준으로 최대 한 번만 분리하여 리스트를 생성합니다.
    username, domain = email_address.split('@', 1)

    # 분리된 사용자명과 도메인을 출력합니다.
    print(f"사용자명: {username}")
    print(f"도메인: {domain}")
else:
    print("올바른 이메일 형식이 아닙니다.")