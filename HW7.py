#Given, p, a and b specifying an elliptic curve, output every point on the curve in lexicographical
#order, sorted by x, breaking ties by y.


def EllipticCurve(p,a,b):

    #Step 1: Determining which values of x have matching solutions for y

    for x in range(0,p-1):

        #for all odd primes
        c = ((x**3) + (a*x) + b) % p

        #find if mod equivlant to c mod p
        
        d = (p-1) / 2
        #now uhh do the remeidner part
        #c ^ p-1/2
        e = c**d
        f = int(e % p)
        #print(f'{x} = {e} {f}')
        #now we find the amount of curves
        NumSolutions = 0
        for z in range(-1,2):
            if (z%p) == f:
                if z ==-1:
                   NumSolutions = 0
                elif z == 1:
                    NumSolutions = 2
                elif z == 0:
                    NumSolutions = 1
    
        
        #print(f'{x} = {c} {c% p}')
        
        #Step 2: Determining the matching value of y for a given x that has one.
        #we use the number of soilutions previously calculated here
        match NumSolutions:
            case 2:
                g = int((p+1) / 4)
                c = c **g
                y1 = c % p
                y2 = (y1 - p) * -1

                #determing printing order
                if y1 < y2:
                    print(f'{x} {y1}')
                    print(f'{x} {y2}')
                else:
                    print(f'{x} {y2}')
                    print(f'{x} {y1}')





                
            case 1:
                g = int((p+1) / 4)
                c = c **g
                y1 = c % p
                print(f'{x} {y1}')





def main():
    inputs = input().split(' ')


    p = int(inputs[0])
    a = int(inputs[1])
    b = int(inputs[2])

    print(f"{p} {a} {b}")

    EllipticCurve(p,a,b)

if __name__ == '__main__':
    main()