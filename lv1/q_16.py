# 수박수박수박수박수박수? lv1

# water_melon함수는 정수 n을 매개변수로 입력받습니다.
# 길이가 n이고, 수박수박수...와 같은 패턴을 유지하는
# 문자열을 리턴하도록 함수를 완성하세요.

# 예를들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.


def water_melon(n):
    return ''.join(["수박"[wm%2] for wm in range(n)])
    # return ("수박"*n)[:n]


def q_16():
    print("n이 3인 경우: " + water_melon(3));
    print("n이 4인 경우: " + water_melon(4));
