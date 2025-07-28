while True:
    # 사용자로부터 문장을 입력받습니다.
    original_sentence = input("공백이 포함된 문장을 입력하세요: ")
    
    if not original_sentence:
        print(" 문장을 입력해주세요.\n")
        continue

    # 1. split(): 문장을 공백 기준으로 '분리'하여 단어 리스트로 만듭니다.
    word_list = original_sentence.split()
    print("\n--- 1. split() 실행 결과 ---")
    print(f"분리된 리스트: {word_list}")
    
    # 2. join(): 분리된 리스트를 공백(' ')으로 '결합'하여 다시 문장으로 만듭니다.
    joined_sentence = " ".join(word_list)
    print("\n--- 2. join() 실행 결과 ---")
    print(f"다시 합쳐진 문장: {joined_sentence}")
    
    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 실행하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("=" * 30)