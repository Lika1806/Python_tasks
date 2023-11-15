def create_counter(count = 0):
    def increment():
        nonlocal count
        count+=1
    def decrement():
        nonlocal count
        count-=1
    def get_counter_value():
        return count
    return increment, decrement, get_counter_value

def test():
    inc, dec, get_counter = create_counter(3)
    inc()
    inc()
    inc()
    dec()
    print(get_counter())
    inc()
    inc()
    inc()
    print(get_counter())

test()
