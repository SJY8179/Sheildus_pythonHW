import re
from collections import Counter

def analyze_word_frequency(filename):
    """
    텍스트 파일을 읽어 단어 빈도를 분석하고,
    빈도 순으로 정렬된 리스트를 반환합니다.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read().lower()  # 1. 모두 소문자로 변환

            # 2. 정규표현식으로 한글, 영어, 숫자만 남기고 특수문자 제거
            words = re.findall(r'[가-힣a-z0-9]+', text)
            
            # 3. Counter로 단어 빈도 계산
            if not words:
                return None
            
            # 4. 가장 많이 나타난 단어 순으로 정렬하여 반환
            return Counter(words).most_common()

    except FileNotFoundError:
        print(f" '{filename}' 파일을 찾을 수 없습니다.")
        return None
    except IOError as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")
        return None

# --- 메인 프로그램 실행 ---

# 1. 분석할 샘플 파일 생성
file_to_analyze = 'word_freq_test.txt'
sample_content = """
파이썬은 배우기 쉬운 프로그래밍 언어입니다.
효율적인 파이썬 프로그래밍 능력은 중요합니다.
파이썬은 강력한 데이터 분석 언어!
"""
try:
    with open(file_to_analyze, 'w', encoding='utf-8') as f:
        f.write(sample_content)
except IOError:
    print("샘플 파일 생성에 실패했습니다.")


# 2. 단어 빈도 분석 함수 호출
word_counts = analyze_word_frequency(file_to_analyze)

# 3. 결과 출력
if word_counts:
    print("---  단어 빈도 분석 결과 ---")
    for word, count in word_counts:
        print(f"{word}: {count}번")