def memory_init(frames):
    return dict(memory = [], pages = [], free_index = 0, frame_number = frames)

def access_page (memory, page):
    if page in memory['pages']:
        return True
    return False

def allocate_page(memory, *pages):
    def valid_page(page):
        if page in memory['pages']:
            print(f"The page {page} is already allocated: ")
            return False
        if page > page_number:
            print(f"The page {page} doesn't exist: ")
            return False
        return True

    for page in pages:
        if not valid_page(page):
            continue
        if memory['free_index'] == memory['frame_number']:  
            memory['memory'].pop(0)
            memory['free_index']-=1
            memory['pages'].pop(0)
        memory['memory'].append(page_list[page])
        memory['free_index']+=1
        memory['pages'].append(page)


def display_status(memory):
    for i,page in enumerate(memory['pages']):
        print(f'Frame {i}: Page {page}')


def test_code():
    print("TEST STAR\n")
    my_memory = memory_init(frame_number)
    print("Allocating page 3")
    allocate_page(my_memory, 3)
    display_status(my_memory)
    print("Allocating pages 3,4,5,6")
    allocate_page(my_memory, 3,4,5,6)
    display_status(my_memory)
    print("Allocating pages 7, 25, 17")
    allocate_page(my_memory, 7, 45, 17)
    display_status(my_memory)
    print("Allocating pages 56, 1, 19")
    allocate_page(my_memory, 56, 1, 19)
    display_status(my_memory)
    print("accessing page 4")
    print(access_page(my_memory,4))
    print("accessing page 2")
    print(access_page(my_memory,2))
    print("\nTEST END")



frame_number = 5
page_number = 20
page_list = list('page'+str(n) for n in range(page_number))

test_code()
