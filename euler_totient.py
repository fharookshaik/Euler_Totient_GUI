def gcd(x,y):
    '''
    Returns the gcd(x,y)
    '''
    try:
        if x == 0:
            return y
        if y == 0:
            return x

        if x == y:
            return x

        if x > y :
            return gcd(x-y,y)
        return gcd(x,y-x)

    except Exception as e:
        print('Error calculating GCD: ' + str(e))

def Euler_totient(num):
    '''
        Return the euler totient values and count of a num
    '''
    try:
        l = []
        for i in range(num):
            if gcd(num,i) == 1:
                l.append(i)
            
        return len(l),l

    except Exception as e:
        print('Error finding Euler Totient: '+ str(e))

if __name__ == '__main__':
    n = int(input("Enter the number to find the euler's totient values: "))
    count, values = Euler_totient(n)
    print('The number {} has {} euler totient values.\nValues = {}'.format(n,count,values))