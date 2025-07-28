def process_order(order_id, *items, **customer_info):
    print(f"--- 주문번호: {order_id} ---")
    
    print(">> 주문 상품 목록 (args):")
    for item in items:
        print(f"  - {item}")
        
    print(">> 고객 정보 (kwargs):")
    for key, value in customer_info.items():
        print(f"  - {key}: {value}")

print("## 종합 예제 ##")
process_order(
    20250728, 
    '노트북', '마우스', '키보드', 
    customer_name='정하은', 
    address='경기도 용인시'
)