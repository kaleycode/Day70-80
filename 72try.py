from replit import db
import os, time, datetime, random

def newUser():
  username = input("Creat Username: ")
  password = input("Create Password: ")
  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  db[username] = {"password": newPassword, "salt": salt}
  print()
  print("User Stored")
  time.sleep(1.7)
  os.system("clear")
  login()

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print()
    print("Incorrect Information")
    time.sleep(1.5)
    os.system("clear")
    return
  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  if db[username]["password"]==newPassword:
    print("Logged in")
    print()
    mainMenu()

def mainMenu():
  time.sleep(1)
  os.system("clear")
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
  mainMenu()

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
      carryOn = input("Next entry? (yes or no):\n> ")
      print()
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")
  mainMenu()


while True:
  keys = db.keys()
  for key in keys:
    del db[key]
  print("Day 72: Secret Diary")
  print()
  print("Login\n")
  keys = db.keys()
  if len(keys)<1:
    newUser()
    time.sleep(1)
    os.system("clear")
  elif len(keys)>0:
    login()
