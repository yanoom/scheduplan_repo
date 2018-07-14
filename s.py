import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

def print_menu():
   "Prints menu"
   print("Welcome to scheduplan beta0.1")
   return

def read_input(type, prompt):
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
print_menu()
print("1- insert new task")
print("2- print task by id")
print("3- print all tasks")
selection = read_input("int", "Please select an option:")
print("selection = ", str(selection))
if (1 == selection):
    new_task = {"name":"new task"}
    new_task_id = db.tasks.insert_one(new_task).inserted_id
    print_task_by_obj(new_task_id)
if (2 == selection):
    print_task_by_obj(ObjectId('5b492a337906a400e4280ea3'))
if (3 == selection):
    print("*** All tasks ***\n*** ***")
    for task in db.tasks.find():
        pprint.pprint(task)
        print("------")