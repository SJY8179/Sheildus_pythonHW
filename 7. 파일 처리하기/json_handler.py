import json

# 1. 파일에 저장할 샘플 데이터 (파이썬 딕셔너리)
user_data = {
    "name": "김철수",
    "age": 25,
    "job": "개발자",
    "hobbies": ["독서", "영화감상", "코딩"],
    "address": "서울시 강남구"
}

# 저장할 파일 이름
filename = "data.json"

# --- JSON 파일에 쓰기 (Writing) ---
try:
    with open(filename, 'w', encoding='utf-8') as f:
        # json.dump()를 사용하여 딕셔너리를 파일에 씁니다.
        # ensure_ascii=False: 한글을 그대로 저장합니다.
        # indent=4: 가독성을 위해 4칸 들여쓰기로 저장합니다.
        json.dump(user_data, f, ensure_ascii=False, indent=4)
    
    print(f"'{filename}'에 데이터가 저장되었습니다.")

except IOError as e:
    print(f"파일 저장 중 오류가 발생했습니다: {e}")


# --- JSON 파일에서 읽어오기 (Reading) ---
print("\n--- JSON에서 읽어온 데이터 ---")
try:
    with open(filename, 'r', encoding='utf-8') as f:
        # json.load()를 사용하여 파일에서 데이터를 읽어와 파이썬 딕셔너리로 변환합니다.
        loaded_data = json.load(f)
        
        # 읽어온 데이터를 출력합니다.
        print(f"이름: {loaded_data['name']}")
        print(f"나이: {loaded_data['age']}")
        print(f"직업: {loaded_data['job']}")
        print(f"취미: {loaded_data['hobbies']}")
        print(f"주소: {loaded_data['address']}")
        
except FileNotFoundError:
    print(f" '{filename}' 파일을 찾을 수 없습니다.")
except json.JSONDecodeError:
    print(f" '{filename}' 파일이 올바른 JSON 형식이 아닙니다.")
except IOError as e:
    print(f"파일 읽기 중 오류가 발생했습니다: {e}")