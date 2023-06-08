def square(a):
    perimeter = a * 4
    s = a * a
    diagonal = (2 ** 0.5) * a
    res_tup = (perimeter,s,diagonal)
    return res_tup


if __name__ == '__main__':
    print(square(45))
    print(type(square(45)))
