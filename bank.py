def bank(a,years):
    #Базовый случай:
    if years == 0:
        return a
    #Рекурсивный случай:
    else:
        years = years - 1
        a = a * 1.1
        print(a)
        return bank(a,years)


if __name__ == '__main__':
    print(bank(10000, 5))
