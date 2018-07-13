def print_menu():
   "Prints menu"
   print("Welcome to scheduplan")
   return

def read_input():
    try:
        mode=int(input('Input:'))
    except ValueError:
        print("Not a number")
    return mode

print_menu()
selection = read_input()
print("selection = ", str(selection))
