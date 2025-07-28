# 샘플 리스트를 정의합니다.
fruits = ['사과', '바나나', '딸기', '오렌지']

print("--- 기본 enumerate 사용 (인덱스 0부터 시작) ---")
for index, fruit in enumerate(fruits):
    print(f"인덱스 {index}: {fruit}")

print("\n--- 'start=1' 옵션 사용 (1부터 시작) ---")
# start 인자를 사용하면 시작 인덱스 번호를 지정할 수 있습니다.
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}번째 과일: {fruit}")