import json

def get_answer(string, answers = {'yes': True, 'no': False}):
    while True:
        answer = input(string).lower()
        if answer in answers:
            return answers[answer]
        print("Input is invalid")

def get_valid_input(string):
    while True:
        input_ = input(string)
        if input_:
            return input_
        print("Input is invalid: ")

def load_json(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File doesn't exist")
        return -1
    except JSONDecodeError:
        print("Could't read the file")
        return -1


def add_data(file):
    data = {}
    try:
        with open(file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        if not get_answer("File doesn't exist, do you want to creat new one?(yes or no): "):
            return -1
    except JSONDecodeError:
        if not get_answer("Couldn't read a file, do you want to overwrite it? (yes or no): "):
            return -1

    key = get_valid_input('Input a key: ')
    value = get_valid_input('Input a value: ')

    if key not in data:
        data[key] = value
    else:
        print("Failed: Existing key")
        return -1
    with open(file, 'w') as f:
        json.dump(data, f)
        print("Done!")
    return 1



def get_data(file):
    data = load_json(file)
    if data == -1:
        return -1
    print(data)
    return 1


def update_data(file):
    data = load_json(file)
    if data == -1:
        return -1

    key = get_valid_input('Input a key: ')
    if key not in data:
        print("The key does not exist")
        return -1

    value = get_valid_input('Input a value: ')
    data[key] = value
    with open(file, 'w') as f:
            json.dump(data, f)
            print("Done!")
    return 1


def del_data(file):
    data = load_json(file)
    if data == -1:
        return -1

    key = get_valid_input('Input a key: ')
    if key not in data:
        print("The key does not exist")
        return -1

    del data[key]
    with open(file, 'w') as f:
        json.dump(data, f)
        print("Done!")
    return 1



all_functions = [add_data, get_data, update_data, del_data]

file_name = get_valid_input("Write file name: ")

print("Choose operation from list:")
print("1: add_data")
print("2: get_data")
print("3: update_data")
print("4: del_data")
print("!: exit")

while True:
    answer = input()
    if answer == '!':
        break
    if answer in ('1', '2', '3', '4'):
        all_functions[int(answer)-1](file_name)
    else:
        print("Invalid input")
                    
