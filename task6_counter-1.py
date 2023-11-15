def create_counter(count = 0):
    def increment():
        nonlocal count
        count+=1
    def decrement():
        nonlocal count
        count-=1
    return increment, decrement

def get_counter_value(foo):
    return foo.__closure__[0].cell_contents


def test():
    inc, dec = create_counter(3)
    inc()
    inc()
    inc()
    dec()
    print(get_counter_value(inc))
    inc()
    inc()
    inc()
    print(get_counter_value(dec))

test()
