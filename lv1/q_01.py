# 행렬의 덧셈 lv1
def sumMatrix(A,B):
    answer = []
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

def q_01():
    print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))