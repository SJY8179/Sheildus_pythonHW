# 사용자로부터 문장을 입력받습니다.
sentence = input("문장을 입력하세요: ")

# 1. 공백 제거
# replace() 메서드를 사용하여 모든 공백(' ')을 빈 문자열('')로 바꿉니다.
no_space_sentence = sentence.replace(' ', '')

# 2. 단어 개수 세기
# split() 메서드는 공백을 기준으로 문장을 나누어 단어의 리스트를 만듭니다.
# len() 함수로 이 리스트의 길이를 세어 단어의 개수를 구합니다.
word_count = len(sentence.split())

# 결과를 출력합니다.
print(f"\n공백 제거 결과: {no_space_sentence}")
print(f"총 단어 수: {word_count}개")