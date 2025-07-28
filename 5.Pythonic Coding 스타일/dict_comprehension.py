# 1부터 10까지의 숫자를 사용하여 딕셔너리를 만듭니다.
# for x in range(1, 11): 1부터 10까지의 숫자를 순회
squared_dict = {x: x**2 for x in range(1, 11)}

# 생성된 딕셔너리를 출력합니다.
print("숫자와 그 제곱값의 딕셔너리:")
print(squared_dict)