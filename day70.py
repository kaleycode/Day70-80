import os, time
while True:
  print("⭐️ Day 70: Login System ⭐️")
  print()
  login = input("Login: ")
  if login == "admin":
    adminPass = input("Password: ")
    adminpass = os.environ['adminpass']
    if adminpass == adminPass:
      print("Welcome, Admin!")
      break
    else:
      print("Wrong password")
  elif login == "user":
    userPass = input("Password: ")
    userpass = os.environ['userpass']
    if userpass == userPass:
      print("Welcome, Normie!")
      break
    else:
      print()
      print("Wrong password")
      print()
      time.sleep(1)
      os.system("clear")
  else:
    print("Wrong login")
    time.sleep(1)
    os.system("clear")


#the shorter way from the solution looks like this:
#while True:
  #username = input("Username: ")
  #password = input("Password: ")
  #if username == os.environ['adminUsername'] and password == os.environ['adminPassword']:
  #  print("Welcome Admin")
 #   break
 # elif username ==  os.environ['username'] and password == os.environ['password']:
 #   print("Welcome Normy")
 #   break
 # else:
 #   print("Try again")