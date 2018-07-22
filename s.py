import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
from enum import Enum

local_db = True
remote_db = False

class MenuItem(Enum):
    INSERT_NEW_TASK = 1
    PRINT_TASK_BY_ID = 2
    EDIT_TASK = 3
    DELETE_TASK_BY_ID = 4
    PRINT_ALL_TASKS = 5
    SUMMARIZE_PERIOD_OF_TIME = 6
    QUIT = 7

def function_to_be_called():
    print("I was here!!  ;)")

menu_buttons = {'k':["Prompt title", function_to_be_called]}

def print_menu():
   "Prints menu"
   for (option o in menu_buttons):
       print(o[0], "- ")

   # print("1- Insert new task")
   # print("2- Print task by id")
   # print("3- Edit task")
   # print("4- Delete task by id")
   # print("5- Print all tasks")
   # print("6- Summarize period of time")
   # print("Q- Quit")
   # menu_obj = {}
   # menu_obj += {'action':'k', 'prompt':'Do special action', 'function':}

def read_input(prompt, type="string"):
    if ("int" == type):
        try:
            mode=int(input(prompt))
        except ValueError:
            print("Not a number")
    else:
        mode = input(prompt)
    return mode

def db_init(local=True):
    if (local):
        client = MongoClient('localhost', 27017)
    else:
        client = MongoClient('atlas.mongodb.org/yanoom', 27017)  #TODO: Insert connection string
    db_handler = client.scheuplan_db
    print("db init succeeded")
    return db_handler

def print_task_by_name(task_name):
    pprint.pprint(db.tasks.find_one({'name': task_name}))

def print_task_by_obj(task_obj):
    try:
        pprint.pprint(db.tasks.find_one({'_id': task_obj}))
    except:
        print("Error occured, probably id does not exist!")


print("Welcome to scheduplan beta0.1")
db = db_init(local_db)

selection = 0
while (('q' != selection) and ('Q' != selection)):
    print_menu()
    selection = read_input("Please select an option:")
    print("selection = ", selection)

    try:
        print("option = ", menu_buttons[selection][0])
        menu_buttons[selection][1]()
    except:
        print("Please select a valid option from the menu")

    if ('1' == selection):
        new_name = read_input("Please insert a name for new task: ")
        new_task = {"name":new_name}
        new_task_id = db.tasks.insert_one(new_task).inserted_id
        print_task_by_obj(new_task_id)
    if ('2' == selection):
        obj_id = read_input("Please insert ObjectId: ")
        print_task_by_obj(ObjectId(obj_id))
    if ('4' == selection):
        obj_id = read_input("Please insert ObjectId: ")
        print_task_by_obj(ObjectId(obj_id))
        del_assert = read_input("Delete? (y/Y to accept)")
        if(('y' == del_assert) or ('Y' == del_assert)):
            db.tasks.delete_one({'_id': ObjectId(obj_id)})
    if ('5' == selection):
        print("*** All tasks ***\n*** ***")
        for task in db.tasks.find():
            pprint.pprint(task)
            print("------")