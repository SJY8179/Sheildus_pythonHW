# 원본 숫자 리스트를 정의합니다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트 컴프리헨션을 사용하여 짝수만 제곱합니다.
# [ 최종값 for 요소 in 리스트 if 조건 ]
squared_evens = [n**2 for n in numbers if n % 2 == 0]

# 결과를 출력합니다.
print(f"원본 리스트: {numbers}")
print(f"짝수만 제곱한 결과: {squared_evens}")