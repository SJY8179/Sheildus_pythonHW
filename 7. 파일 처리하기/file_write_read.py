# 1. 파일에 내용 쓰기 (Writing)

# 저장할 파일 이름과 내용을 리스트로 정의합니다.
filename = "my_notes.txt"
lines_to_write = [
    "파이썬 파일 쓰기 예제입니다.",
    "두 번째 줄입니다.",
    "with 구문을 사용하면 편리합니다."
]

# 'w' 모드(쓰기 모드)로 파일을 엽니다.
# encoding='utf-8'은 한글이 깨지지 않게 해줍니다.
try:
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines_to_write:
            f.write(line + '\n')  # 각 줄 끝에 줄바꿈(\n)을 추가합니다.

    print(f" '{filename}' 파일에 성공적으로 저장했습니다.")

except IOError as e:
    print(f"파일 저장 중 오류가 발생했습니다: {e}")


# 2. 파일 내용 읽어오기 (Reading)

print("\n--- 파일 내용 읽기 ---")
# 'r' 모드(읽기 모드)로 파일을 엽니다.
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()  # 파일의 전체 내용을 하나의 문자열로 읽어옵니다.
        print(content)
        
except FileNotFoundError:
    print(f" '{filename}' 파일을 찾을 수 없습니다.")
except IOError as e:
    print(f"파일 읽기 중 오류가 발생했습니다: {e}")