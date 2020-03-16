m = 'Its visible everywhere'


def a():
    ma = 'Its visible in b() and a()'

    def b():
        print(m)
        print(ma)
        mb = 'Its visible in c() and b(), but dont visible in a()'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'Its visible in c() only'

        # print(mc)  # The result will be Error, because 'mc' is local var of function c
        c()

    b()


a()
