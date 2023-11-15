def creat_note(book):
    def input_note():
        while True:
            note = input("input a note: ")
            if note: return note
            print("Input was invalid, try again: ")
    global id_counter
    book[id_counter] = input_note()
    id_counter+=1
    print("The note was successfully added!")

def list_notes(book):
    for id_, note in book.items():
        print(f"{id_:}  {note[:10]}...")

def get_note(book):
    id_ = input("input ID: ")
    try:
        print(book[int(id_)])
    except (ValueError, KeyError):
        print("Don't have such note: ")

def remove_note(book):
    id_ = input("input ID: ")
    try:
        del book[int(id_)]
        print("The note was successfully removed!")
    except (ValueError, KeyError):
        print("Don't have such note: ")

def search_note(book):
    word = input("input the word to search: ").lower()
    found = False
    for key, value in book.items():
        index = value.lower().find(word)
        if index!=-1:
            print(f"{key}: {value[:index]} <<<{value[index:index+len(word)]}>>> {value[index+len(word):]}")
            found = True
    if not found:
        print("dind't find any matches:")
    



all_functions = [creat_note, get_note, remove_note, search_note, list_notes]
my_notes = {}
id_counter = 1

print("Choose what to do")
print("1: creat_note")
print("2: get_note")
print("3: remove_note")
print("4: serach by a word")
print("5: list all notes")
print("!: to exit")

while True:
    answer = input()
    if answer == '!':
        break
    if answer in ('1', '2', '3', '4', '5'):
        all_functions[int(answer)-1](my_notes)
    else:
        print("input was invalid")
