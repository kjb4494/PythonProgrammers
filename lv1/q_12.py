# 문자열 다루기 기본

# alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.
# s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.
# 예를들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다

def alpha_string46(s):
    for i in s:
        if i not in ['1','2','3','4','5','6','7','8','9','0']:
            return "False"
    return len(s) in [4, 6]

    # isdigit를 활용
    # return s.isdigit() and len(s) in [4, 6]


def q_12():
    print( alpha_string46("a234") )
    print( alpha_string46("1234") )
