def Positive(P):
    while True:
        try:
            value = float(input(P))
            if value > 0:
                return value
            print("양수를 입력하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def Discount_rate(P):
    while True:
        try:
            value = float(input(P))
            if 0 <= value <= 100:
                return value
            print("할인율은 0~100 사이로 입력하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

def Discounted_price(price, discount_rate):
    return price * (1 - discount_rate / 100)

def main():
    price = Positive("상품의 가격을 입력하세요: ")
    discount_rate = Discount_rate("할인율(%)을 입력하세요: ")
    discounted = Discounted_price(price, discount_rate)
    print(f"할인된 가격: {discounted:.2f}원")

if __name__ == "__main__":
    main()
