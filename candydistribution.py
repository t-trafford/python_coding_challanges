

# candy problem
t = [3, 4]

def solution(t):
    # write your code in Python 3.6
    mid = len(t)/2
    kida = set([])
    for i in range(0, len(t)):
        if i not in kida:
            kida.add(t[i])

    dup = len(t)-len(kida)
    need = mid - dup
    actual = len(kida) -need

    print(actual)

solution(t)