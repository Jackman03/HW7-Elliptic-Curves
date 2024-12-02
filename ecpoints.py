#Jackson Vaughn
#CIS3362
#Homework 7
#Given, p, a and b specifying an elliptic curve, output every point on the curve in lexicographical
#order, sorted by x, breaking ties by y.


def EllipticCurve(p,a,b):

    #Step 1: Determining which values of x have matching solutions for y
    for x in range(0,p):

        #c is used to detect th amount of co
        c = ((x**3) + (a*x) + b) % p

        #find if mod equivlant to c mod p
        
        d = (p-1) // 2
        #now uhh do the remeidner part
        #c ^ p-1/2
        f = pow(c,d,p)
        #Used to find the number of solutions
        NumSolutions = 0
        
        #If this remainder is 1, then we know there are two values of y on the curve for this particular value of x.
        if f == 1:
            NumSolutions = 2
            
        elif f == 0:
            NumSolutions = 1
            #If we get p – 1, then we can skip over this value of x
        elif f == p-1:
            NumSolutions = 0
    
        #Step 2: Determining the matching value of y for a given x that has one.
        #we use the number of soilutions previously calculated here
        match NumSolutions:
            case 2:
                g = (p+1) // 4
                y1 = pow(c,g,p)
                #To get the other value of y, just subtract the original solution for y above from p
                y2 = (p - y1) % p

                #determing printing order
                if y1 < y2:
                    print(f'{x} {y1}')
                    print(f'{x} {y2}')
                else:
                    print(f'{x} {y2}')
                    print(f'{x} {y1}')   
            case 1:
                g = (p+1) // 4
                y1 = pow(c,g,p)

                print(f'{x} {y1}')



def main():
    inputs = input().split(' ')


    p = int(inputs[0])
    a = int(inputs[1])
    b = int(inputs[2])

    EllipticCurve(p,a,b)

if __name__ == '__main__':
    main()