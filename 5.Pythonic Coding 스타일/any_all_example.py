# 검사에 사용할 숫자 리스트들을 정의합니다.
list_a = [10, 25, 30, 45]
list_b = [10, -5, 30, 45]
list_c = [-10, -5, -30, -45]

# --- 1. all() 함수 예제 ---
print("## all() 함수: 모든 조건이 맞아야 True")

# list_a의 모든 요소가 0보다 큰지 검사합니다.
all_positive_a = all(n > 0 for n in list_a)
print(f"{list_a} -> 모든 숫자가 0보다 큰가?   {all_positive_a}")

# list_b의 모든 요소가 0보다 큰지 검사합니다. (-5 때문에 False)
all_positive_b = all(n > 0 for n in list_b)
print(f"{list_b} -> 모든 숫자가 0보다 큰가?   {all_positive_b}")

print("-" * 40)

# --- 2. any() 함수 예제 ---
print("## any() 함수: 하나라도 조건이 맞으면 True")

# list_b에 0보다 작은 숫자가 하나라도 있는지 검사합니다. (-5 때문에 True)
any_negative_b = any(n < 0 for n in list_b)
print(f"{list_b} -> 0보다 작은 숫자가 하나라도 있는가?   {any_negative_b}")

# list_a에 0보다 작은 숫자가 하나라도 있는지 검사합니다. (없으므로 False)
any_negative_a = any(n < 0 for n in list_a)
print(f"{list_a} -> 0보다 작은 숫자가 하나라도 있는가?{any_negative_a}")