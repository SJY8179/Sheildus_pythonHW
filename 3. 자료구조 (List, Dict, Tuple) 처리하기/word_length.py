while True:
    # 사용자로부터 공백으로 구분된 단어들을 입력받습니다.
    input_str = input("단어들을 공백으로 구분하여 입력하세요 (예: apple banana cherry): ")
    
    # 입력받은 문자열을 공백 기준으로 나누어 리스트로 만듭니다.
    words = input_str.split()
    
    # 입력된 단어가 있는지 확인합니다.
    if not words:
        print("\n 하나 이상의 단어를 입력해주세요.\n")
        continue

    # key=len을 사용하여 길이를 기준으로 최댓값(가장 긴 단어)을 찾습니다.
    longest_word = max(words, key=len)
    
    # key=len을 사용하여 길이를 기준으로 최솟값(가장 짧은 단어)을 찾습니다.
    shortest_word = min(words, key=len)
    
    # --- 결과 출력 ---
    print(f"\n입력된 단어들: {words}")
    print("-" * 30)
    print(f" 가장 긴 단어: '{longest_word}' (길이: {len(longest_word)})")
    print(f"가장 짧은 단어: '{shortest_word}' (길이: {len(shortest_word)})")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)