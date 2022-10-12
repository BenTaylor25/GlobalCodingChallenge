def _divisors(inp, a, b):
    # a = low
    # b = high
    # IF a*b < inp THEN increase a
    # IF a*b > inp THEN decrease b
    # IF a*b == inp THEN a and b are divisors

    # stopping condition
    if a > b:
        return 0

    dvsrs_buffer = 0
    c = a*b
    if c < inp:
        dvsrs_buffer += _divisors(inp, a+1, b)
    elif c > inp:
        dvsrs_buffer += _divisors(inp, a, b-1)
    else:
        dvsrs_buffer += (a & 1) * -2 + 1
        if b != a:
            dvsrs_buffer += (b & 1) * -2 + 1

    return dvsrs_buffer

def divisors(inp):
    # dvsrs_buffer: num_of_even_divisors - num_of_odd_divisors (0: even, >0: more even, <0: less even)
    # `(x & 1) * -2 + 1`: 
    #     `(x & 1)`: if_even: 0, if_odd: 1
    #     `(x & 1) * -2`: if_even: 0, if_odd: -2
    #     `(x & 1) * -2 + 1`: if_even: 1, if_odd: -1 
    dvsrs_buffer = (inp & 1) * -2 + 1
    dvsrs_buffer += _divisors(inp, 2, inp<<1)
    
    return dvsrs_buffer

def solution(inp):
    buffer = divisors(inp)
    return "BUY" if buffer > 1 else "SELL" if buffer < 1 else "PASS"

def main():
    inp = int(input("->"))
    print(solution(inp))

if __name__ == '__main__':
    main()

