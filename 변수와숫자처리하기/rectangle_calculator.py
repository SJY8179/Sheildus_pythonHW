def Positive(P):
    while True:
        try:
            val = float(input(P))
            if val > 0:
                return val
            print("양수를 입력하세요.")
        except ValueError:
            print("숫자를 다시 입력하세요.")

def calculate_rectangle(width, height):
    return width * height, 2 * (width + height)

def main():
    w = Positive("가로 길이: ")
    h = Positive("세로 길이: ")
    area, perimeter = calculate_rectangle(w, h)

    print(f"넓이: {area:.2f}")
    print(f"둘레: {perimeter:.2f}")

if __name__ == "__main__":
    main()
