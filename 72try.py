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
    time.sleep(1.5)
    os.system("clear")
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
  print("Login\n")
  for keys in db.keys():
    for key in keys:
      if keys < 1:
        newUser()
        time.sleep(1)
        os.system("clear")
  else:
      login()