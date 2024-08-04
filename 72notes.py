#first attempt from day 72

from replit import db
import os, time, datetime, random
def newUser():
  print()
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("That username is already taken.")
    return
  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  db[username] = {"password": newPassword, "salt": salt}
  print()
  print("Details Stored")
  time.sleep(1.7)
  os.system("clear")
def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print()
    print("That username does not exist")
    return
  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  if db[username]["password"]==newPassword:
    print("Logged in")
    time.sleep(1.7)
    os.system("clear")
    print()
    mainMenu()


def mainMenu():
  menu = input("1: Add an entry\n2: View entries\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()

def add():
  thought = input("Diary entry:\n> ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = thought
  time.sleep(1)
  os.system("clear")

def view():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%1==0):
      carryOn = input("See next entry? (yes or no):\n> ")
      print()
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")

while True:
  print("Day 72: Secret Diary")
  print()
  for key in db.keys():
    if key <= 0:
       newUser()
    else:
      login()
    # I messed up above -- it should check the length like this to see if it's the first time:
      #keys = db.keys()
    # if len(keys)<1:



#Here is the solution from replit: 

from replit import db
import datetime, os, time, random
def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry
def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
      break
keys = db.keys()
if len(keys)<1: #checking to see if it's the first time
  print("First Run > Create account")
  username = input("Username > ")
  password = input("Password > ")
  salt = random.randint(0,9999999)
  newPassword = hash(f"{password}{salt}")
  db[username] = {"password": newPassword, "salt": salt}
else:
  print("Log in")
  username = input("Username > ")
  password = input("Password > ")
  if username not in keys:
    print("Username or password incorrect")
    exit()
  salt = db[username]["salt"]
  newPassword = hash(f"{password}{salt}")
  if db[username]["password"]!=newPassword:
    print("Username or password incorrect")
    exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()
