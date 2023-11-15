import random

def get_valid_input(string):
    while True:
        input_ = input(string)
        if input_:
            return input_
        print ('Input is invalid, try again')

   
def add_task(ls):
    def get_id():
        while True:
            if (new_id := random.choice('ABCD')+str(random.randint(0,10))) not in ls:
                return new_id
    ls[get_id()] = {'task': get_valid_input('Write a task: '), 'priority': 0, 'complete': False }
    print(">>>The task was successfully added<<<")


def remove_task(ls):
    print("------")
    id_ = get_valid_input('Write ID of a task: ')
    try:
        del ls[id_]
        print(">>> The task was successfully removed <<<")
    except KeyError:
        print(">>>Couldn't find that task<<<")

def list_tasks(ls):
    def get_answer(string):
        answers = {'yes': True, 'no': False}
        while True:
            answer = input(string).lower()
            if answer in answers:
                return answers[answer]
    
    sort = get_answer('Do you want to sort by priority(yes or no)? ')
    seperate=get_answer('Do youwant to get compelete and pending tasks seperately (yes or no)? ')
 
    if sort:
        ls = dict(sorted(ls.items(), key = lambda x: x[1]['priority']))
    if not seperate:
        for key, value in ls.items():
            i = 'completed' if value['complete'] else 'pending'
            print(f"{key}:  {value['task']}: {i}")
        return

    pending_tasks = [key for key in ls.keys() if not ls[key]['complete']] 
    completed_tasks = [key for key in ls.keys() if ls[key]['complete']]
    print("\n\nPending tasks")
    for key in pending_tasks:
        print(f"{key}:  {ls[key]['task']}")
    print("\n\nCompleted tasks")
    for key in completed_tasks:
        print(f"{key}:  {ls[key]['task']}")

def mark_complete(ls):
    print("------")
    id_ = get_valid_input('Write ID of a task: ')
    try:
        ls[id_]['complete'] = True
        print(">>>The task is successfully completed !!!<<<")
    except KeyError:
        print(">>>Couldn't find that task<<<")

def set_priority(ls):
    print("------")
    id_ = get_valid_input('Write ID of a task: ')
    number = input("What priority to set? (0: low, 1: medium, 2: high) ")
    while True:
        if number in ('0','1','2'):
            try:
                ls[id_]['priority'] = int(number)
                print(">>> The priority is set<<<")
            except KeyError:
                print(">>>Couldn't find that task<<<")
            finally:
                return
        else:
            number = input("Input is invalid: Try again:")




     
my_list = {}
func_list = [add_task, remove_task, mark_complete, set_priority, list_tasks]

print("What you want to do? ")
print("1: to add task")
print("2: to remove_task")
print("3: to mark task as completed")
print("4: to add priority to a task")
print("5: to list tasks")
print("!: to exit")
 
while True:
    print("___________________")
    answer = input()
    if answer == '!':
        break
    elif answer in ('1','2','3','4','5'):
        func_list[int(answer)-1](my_list)
    else:
        print('input is invalid,try again')
   
