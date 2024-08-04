from replit import db
import time, os, random

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

while True:
  print("Day 71: Login System")
  print()
  print("1: Add User\n2: Login")
  print()
  choice = input("> ")
  if choice == "1":
    newUser()
  elif choice == "2":
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])
      print()