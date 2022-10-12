def _divisors(inp, a, b):


    dvsrs_buffer = 0
    

    return dvsrs_buffer

def divisors(inp):
    # dvsrs_buffer: num_of_even_divisors - num_of_odd_divisors (0: even, >0: more even, <0: less even)
    # `(x & 1) * -2 + 1`: 
    #     `(x & 1)`: if_even: 0, if_odd: 1
    #     `(x & 1) * -2`: if_even: 0, if_odd: -2
    #     `(x & 1) * -2 + 1`: if_even: 1, if_odd: -1 
    dvsrs_buffer = (inp & 1) * -2 + 1
    
    # a = low
    # b = high
    # IF a*b < inp THEN increase a
    # IF a*b > inp THEN decrease b
    # IF a*b == inp THEN a and b are divisors
    a = 2
    b = inp<<1
    while a <= b:
        c = a*b
        print(c)

        if c < inp:
            a += 1
        elif c > inp:
            b -= 1
        else:
            dvsrs_buffer += (a & 1) * -2 + 1
            if b != a:
                dvsrs_buffer += (b & 1) * -2 + 1

            a += 1
            b -= 1
    
    return dvsrs_buffer

def solution(inp):
    buffer = divisors(inp)
    return "BUY" if buffer > 1 else "SELL" if buffer < 1 else "PASS"

def main():
    inp = int(input("-> "))
    print(solution(inp))

if __name__ == '__main__':
    main()

