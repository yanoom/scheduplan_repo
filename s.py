import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

def print_menu(print_welcome=False):
   "Prints menu"
   if(print_welcome):
        print("Welcome to scheduplan beta0.1")
   print("1- insert new task")
   print("2- print task by id")
   print("3- print all tasks")
   print("Q- Quit")

def read_input(prompt, type="string"):
    if ("int" == type):
        try:
            mode=int(input(prompt))
        except ValueError:
            print("Not a number")
    else:
        mode = input(prompt)
    return mode

def db_init():
    client = MongoClient('localhost', 27017)
    new_db = client.scheuplan_db
    print("db init succeeded")
    return new_db

def print_task_by_name(task_name):
    pprint.pprint(db.tasks.find_one({'name': task_name}))

def print_task_by_obj(task_obj):
    pprint.pprint(db.tasks.find_one({'_id': task_obj}))

db = db_init()
print_menu(True)
selection = 0
while (('q' != selection) and ('Q' != selection)):
    print_menu()
    selection = read_input("Please select an option:")
    print("selection = ", selection)
    if ('1' == selection):
        new_task = {"name":"new task"}
        new_task_id = db.tasks.insert_one(new_task).inserted_id
        print_task_by_obj(new_task_id)
    if ('2' == selection):
        obj_id = read_input("Please insert ObjectId: ")
        print_task_by_obj(ObjectId(obj_id))
    if ('3' == selection):
        print("*** All tasks ***\n*** ***")
        for task in db.tasks.find():
            pprint.pprint(task)
            print("------")