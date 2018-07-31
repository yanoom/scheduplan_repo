import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
from enum import Enum

local_db = False
remote_db = "mongodb+srv://kay:myRealPassword@cluster0.mongodb.net/test"

class dbLocations(Enum):
    LOCAL_DB = 1
    REMOTE_DB = 2

db_location = dbLocations.REMOTE_DB

class MenuItem(Enum):
    INSERT_NEW_TASK = 1
    PRINT_TASK_BY_ID = 2
    EDIT_TASK = 3
    DELETE_TASK_BY_ID = 4
    PRINT_ALL_TASKS = 5
    SUMMARIZE_PERIOD_OF_TIME = 6
    QUIT = 7

def function_to_be_called():
    print("Dummy function!!  ;)")

def print_task_by_obj(task_obj):
    try:
        pprint.pprint(db.tasks.find_one({'_id': task_obj}))
    except:
        print("Error occured, probably id does not exist!")

def menu_action_quit():
    print("Bye!")
    #sys.exit()

def menu_action_new_task():
    new_name = read_input("Please insert a name for new task: ")
    new_task = {"name": new_name}
    new_task_id = db.tasks.insert_one(new_task).inserted_id
    print_task_by_obj(new_task_id)

def read_and_validate_obj_id():
    obj_id = read_input("Please insert ObjectId: ")
    return obj_id

def menu_action_print_task_by_id():
    obj_id = read_and_validate_obj_id()
    print_task_by_obj(ObjectId(obj_id))

def menu_action_edit_task_by_id():
    obj_id = read_and_validate_obj_id()
    print("TBD: EDIT MENU")

def menu_action_delete_task_by_id():
    obj_id = read_input("Please insert ObjectId: ")
    print_task_by_obj(ObjectId(obj_id))
    del_assert = read_input("Delete? (y/Y to accept)")
    if(('y' == del_assert) or ('Y' == del_assert)):
        db.tasks.delete_one({'_id': ObjectId(obj_id)})

def menu_action_print_all_tasks():
    print("*** All tasks ***\n*** ***")
    for task in db.tasks.find():
        pprint.pprint(task)
        print("------")

# menu_buttons = {'k':["Prompt title", function_to_be_called]}
menu_buttons = dict([('1', ["Insert new task", menu_action_new_task]),
                     ('2', ["Print task by id", menu_action_print_task_by_id]),
                     ('3', ["Edit task", function_to_be_called]),
                     ('4', ["Delete task by id", menu_action_delete_task_by_id]),
                     ('5', ["Print all tasks", menu_action_print_all_tasks]),
                     ('6', ["Summarize period of time", function_to_be_called]),
                     ('Q', ["Quit", function_to_be_called]),])

def print_menu():
   "Prints menu"
   for key, value in menu_buttons.items():
       print(key, "- ", value[0])

def read_input(prompt, type="string"):
    if ("int" == type):
        try:
            mode=int(input(prompt))
        except ValueError:
            print("Not a number")
    else:
        mode = input(prompt)
    return mode

def db_init(db_location):
    if (dbLocations.LOCAL_DB == db_location):
        client = MongoClient('localhost', 27017)
    else:
        client = MongoClient("mongodb://yanoom:666@cluster0.mongodb.net/test")
        db_mongo = client.test
        # Issue the serverStatus command and print the results #reference: https://dzone.com/articles/getting-started-with-python-and-mongodb
        serverStatusResult = client.admin.command("serverStatus")
        pprint(serverStatusResult)
    db_handler = client.scheuplan_db
    if (db_handler):
        print("db init succeeded")
    else:
        print("db init failed")
    return db_handler

def print_task_by_name(task_name):
    pprint.pprint(db.tasks.find_one({'name': task_name}))

print("Welcome to scheduplan beta0.1")
#db = db_init(dbLocations.REMOTE_DB)
db = db_init(dbLocations.LOCAL_DB)

selection = 0
while (('q' != selection) and ('Q' != selection)):
    print_menu()
    selection = read_input("Please select an option:").upper()
    #validate selection
    if (selection in menu_buttons.keys()):
        menu_buttons[selection][1]()
    else:
        print("Invalid Selection! Available menu options: ", str(menu_buttons.keys()))
    #perform action:

#TODO: Dynamic menu
#    try:
#        print("option = ", menu_buttons[selection][0])
#        #menu_buttons[selection][1]()
#    except:
#        print("Please select a valid option from the menu")

#review: Static menu
#    if ('1' == selection):
#        new_name = read_input("Please insert a name for new task: ")
#        new_task = {"name":new_name}
#        new_task_id = db.tasks.insert_one(new_task).inserted_id
#        print_task_by_obj(new_task_id)
#    if ('2' == selection):
#        obj_id = read_input("Please insert ObjectId: ")
#        print_task_by_obj(ObjectId(obj_id))
#     if ('4' == selection):
#         obj_id = read_input("Please insert ObjectId: ")
#         print_task_by_obj(ObjectId(obj_id))
#         del_assert = read_input("Delete? (y/Y to accept)")
#         if(('y' == del_assert) or ('Y' == del_assert)):
#             db.tasks.delete_one({'_id': ObjectId(obj_id)})
#     if ('5' == selection):
#         print("*** All tasks ***\n*** ***")
#         for task in db.tasks.find():
#             pprint.pprint(task)
#             print("------")
