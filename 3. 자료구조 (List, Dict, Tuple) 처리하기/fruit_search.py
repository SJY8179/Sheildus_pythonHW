# 검색할 과일 리스트를 미리 정의합니다.
fruit_list = ["사과", "바나나", "딸기", "오렌지", "포도", "수박", "멜론"]

while True:
    # 사용자로부터 검색할 과일 이름을 입력받습니다.
    search_fruit = input("검색할 과일 이름을 입력하세요: ")

    # 'in' 연산자를 사용하여 리스트에 과일이 있는지 확인합니다.
    if search_fruit in fruit_list:
        print(f"\n🎉 네, '{search_fruit}'은(는) 목록에 있습니다.")
    else:
        print(f"\n😥 아쉽지만 '{search_fruit}'은(는) 목록에 없습니다.")

    # 사용자에게 다시 실행할지 묻습니다.
    if input("\n다시 검색하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("-" * 30)