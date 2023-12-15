def bla(*blah):
    for i in blah:
        print(i)
bla(*[i for i in range(5)])
del bla
