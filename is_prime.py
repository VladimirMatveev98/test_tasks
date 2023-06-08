def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
             if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    print(is_prime(7)) #True
    print(is_prime(15)) #False

    """for i in range(1,1000):
        print(is_prime(i))"""
