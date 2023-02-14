def func(x):
    if x == 0:
        return 0
    else:
       x=+ func(x - 1)
       return x
print(func(4))
