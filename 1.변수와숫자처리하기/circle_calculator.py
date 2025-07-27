# 원의 반지름을 입력받음
radius = float(input("원의 반지름을 입력하세요: "))

# π 값
pi = 3.14159

# 원의 넓이 계산
area = pi * radius ** 2

# 원의 둘레 계산
circumference = 2 * pi * radius

# 결과 출력
print(f"원의 넓이: {area}")
print(f"원의 둘레: {circumference}")
