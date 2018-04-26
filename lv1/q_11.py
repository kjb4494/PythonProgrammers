# 자릿수더하기

# sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
# 예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
# sum_digit함수를 완성해보세요.

def sum_digit(number):
    # return sum([int(i) for i in str(number)])

    # map(f, iterable)은 각 요소가 함수 f에 의해
    # 수행된 결과를 묶어서 리턴하는 함수다.
    return sum(map(int, str(number)))

def q_11():
    print("결과 : {}".format(sum_digit(123)));