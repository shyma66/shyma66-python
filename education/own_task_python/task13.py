def zeros(x, lazy=False):
    if lazy:
        for i in range(x):
            print(i)
    return  [0] * x

print(zeros(4, lazy=True))