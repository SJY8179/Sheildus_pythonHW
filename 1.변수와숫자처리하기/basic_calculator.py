while True:
    try:
        x = int(input("첫 번째 정수: "))
        y = int(input("두 번째 정수: "))
        op = input("연산자 (+, -, *, /): ")
        if op not in '+-*/':
            print("연산자를 제대로 선택하세요.")
            continue
        if op == '/' and y == 0:
            print("0으로 나눌 수 없습니다.")
            continue
    except:
        print("정수를 입력해 주세요.")
        continue

    result = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }[op]

    print(f"{x} {op} {y} = {result}")

    if input("계속하려면 Enter, 종료하려면 n: ").lower() == 'n':
        break
