while True:
    # 새로운 쇼핑을 위해 빈 딕셔너리로 카트를 초기화합니다.
    shopping_cart = {}
    total_price = 0

    print("--- 쇼핑 카트에 상품 추가 ---")
    print("상품명에 '완료'를 입력하면 입력을 종료하고 계산합니다.")

    # 상품 추가를 위한 내부 반복문
    while True:
        # 상품명 입력받기
        product = input("추가할 상품명을 입력하세요: ")

        # '완료'를 입력하면 상품 추가를 중단합니다.
        if product == '완료':
            break

        # 상품 가격 입력받기 (숫자가 아니면 다시 입력)
        while True:
            try:
                price = float(input(f"'{product}'의 가격을 입력하세요: "))
                if price < 0:
                    print("⚠️ 가격은 0 이상이어야 합니다.")
                    continue
                shopping_cart[product] = price
                print(f"'{product}'상품이 카트에 담겼습니다.\n")
                break  # 올바른 가격이 입력되면 가격 입력 반복문 탈출
            except ValueError:
                print("⚠️ 가격은 숫자로만 입력해주세요.")
    
    # --- 최종 계산 ---
    print("\n--- 🧾 최종 계산 결과 ---")
    if shopping_cart:
        print("카트에 담긴 상품 목록:")
        # 카트에 담긴 모든 상품과 가격을 출력합니다.
        for product, price in shopping_cart.items():
            print(f"  - {product}: {price:,.0f}원")
        
        # 카트에 담긴 모든 상품의 가격(value)을 더합니다.
        total_price = sum(shopping_cart.values())
        
        print("\n" + "="*25)
        # f-string의 :,.0f 포맷을 이용해 천 단위 쉼표를 넣습니다.
        print(f" 총 합계 금액: {total_price:,.0f}원")
        print("="*25)
    else:
        print("카트에 담긴 상품이 없습니다.")

    # 전체 프로그램을 다시 실행할지 묻습니다.
    if input("\n새로운 쇼핑 카트로 다시 시작하시겠습니까? (y/n): ").lower() != 'y':
        print("프로그램을 종료합니다.")
        break
    print("\n" + "#"*30 + "\n")