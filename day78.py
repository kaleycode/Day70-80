from flask import Flask

app = Flask(__name__)
myReflections = {}

myReflections["78"] = {"link": "https://replit.com/", "date:": "8/6/2024", "reflection": "Flask is really interesting to learn. I feel like I have gained more from this free course than most of my college courses."}

myReflections["77"] = { "link": "https://replit.com/", "date:": "8/6/2024", "reflection": "Fun stuff, but I still don't enjoy CSS that much" }

myReflections["76"] = { "link": "https://replit.com/", "date:": "6/4/2024", "reflection": "I think I struggled a bit here, but I am glad I was already familiar with HTML"}


@app.route('/<pageNumber>')
def index(pageNumber):
  page = ""
  f = open("reflections.html", "r")
  page = f.read()
  f.close()
  reflection = myReflections[pageNumber]["Reflection"]
  print(myReflections)
  page = page.replace("{day}", pageNumber)
  page = page.replace("{date}", myReflections[pageNumber]["date"])
  page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])
  return page


app.run(host='0.0.0.0', port=81)