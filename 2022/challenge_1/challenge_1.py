def _divisors(x, a, b):
    if a > b:
        return 0

    dvsrs = 0
    c = a*b
    if c < x:
        dvsrs += _divisors(x, a+1, b)
    elif c > x:
        dvsrs += _divisors(x, a, b-1)
    else:
        dvsrs += 1 + (a != b) + _divisors(x, a+1, b-1)

    return dvsrs

def divisors(x):
    return 1 + _divisors(x, 2, x<<1)

def solution(x):
    return "wip"

def main():
    x = int(input())
    solution(x)

if __name__ == '__main__':
    main()

