# 서울에서김서방찾기 lv1

# findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.

# seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.


def findKim(seoul):
    kimIdx = seoul.index("Kim")
    # 함수를 완성하세요

    return "김서방은 {}에 있다".format(kimIdx)

def q_04():
    print(findKim(["Queen", "Tod", "Kim"]))