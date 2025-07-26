# 사용자로부터 문자열을 입력받습니다.
user_input = input("문자열을 입력하세요: ")

# 별도의 변수 선언 없이, 내장 함수를 바로 사용하여 결과를 출력합니다.
print(f"대문자 변환: {user_input.upper()}")
print(f"소문자 변환: {user_input.lower()}")
print(f"문자열 길이: {len(user_input)}")